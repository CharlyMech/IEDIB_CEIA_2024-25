import pickle
from flask import Flask, jsonify, request
from churn_predict_service import predict_single

app = Flask("churn-predict")
with open("models/churn-model.pck", "rb") as f:
    dv, model = pickle.load(f)


@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()
    churn, prediction = predict_single(customer, dv, model)
    result = {
        "churn": bool(churn),
        "churn_probability": float(prediction),
    }
    return jsonify(result)


if __name__ == "__main__":
    """ Second request in notes corrected by ChatGPT since was reporting a 400 HTTP code error
	curl --request POST "http://127.0.0.1:8000/predict" \
	--header "Content-Type: application/json" \
	--data-raw '{
		"gender": "female",
		"seniorcitizen": 1,
		"partner": "no",
		"dependents": "no",
		"phoneservice": "yes",
		"multiplelines": "yes",
		"internetservice": "fiber_optic",
		"onlinesecurity": "no",
		"onlinebackup": "no",
		"deviceprotection": "no",
		"techsupport": "no",
		"streamingtv": "yes",
		"streamingmovies": "no",
		"contract": "month-to-month",
		"paperlessbilling": "yes",
		"paymentmethod": "electronic_check",
		"tenure": 1,
		"monthlycharges": 85.7,
		"totalcharges": 85.7
	}'
	"""

    app.run(debug=True, port=8000)

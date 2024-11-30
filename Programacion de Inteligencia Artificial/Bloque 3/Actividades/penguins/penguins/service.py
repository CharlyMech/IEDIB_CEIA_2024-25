import pickle
from flask import Flask, jsonify, request

# Penguin types
penguins = ["Adelie", "Chinstrap", "Gentoo"]


def predict_single(p, dv, model):
    p_std = dv.transform([p])
    y_pred = model.predict(p_std)[0]
    y_prob = model.predict_proba(p_std)[0][y_pred]
    return (y_pred, y_prob)


def predict(dv, model):
    p = request.get_json()
    specie, prob = predict_single(p, dv, model)

    result = {"penguin": penguins[specie], "probability": float(prob)}
    return jsonify(result)


app = Flask("penguins")


@app.route("/predict_lr", methods=["POST"])
def predict_lr():
    with open("models/lr.pck", "rb") as f:
        dv, model = pickle.load(f)
    return predict(dv, model)


@app.route("/predict_svm", methods=["POST"])
def predict_svm():
    with open("models/svm.pck", "rb") as f:
        dv, model = pickle.load(f)
    return predict(dv, model)


@app.route("/predict_dt", methods=["POST"])
def predict_dt():
    with open("models/dt.pck", "rb") as f:
        dv, model = pickle.load(f)
    return predict(dv, model)


@app.route("/predict_knn", methods=["POST"])
def predict_knn():
    with open("models/knn.pck", "rb") as f:
        dv, model = pickle.load(f)
    return predict(dv, model)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

import pickle
from flask import Flask, jsonify, request

# Iris Classes
classes = ["Iris Setosa", "Iris Versicolour", "Iris Virginica"]


def predict_single(flor, sc, model):
    flor_std = sc.transform([[flor["longitud_petal"], flor["amplada_petal"]]])
    y_pred = model.predict(flor_std)[0]
    y_prob = model.predict_proba(flor_std)[0][y_pred]
    return (y_pred, y_prob)


def predict(sc, model):
    flor = request.get_json()
    especie, probabilitat = predict_single(flor, sc, model)

    result = {"flor": classes[especie], "probabilitat": float(probabilitat)}
    return jsonify(result)


app = Flask("iris")


@app.route("/predict_lr", methods=["POST"])
def predict_lr():
    with open("models/lr.pck", "rb") as f:
        sc, model = pickle.load(f)
    return predict(sc, model)


@app.route("/predict_svm", methods=["POST"])
def predict_svm():
    with open("models/svm.pck", "rb") as f:
        sc, model = pickle.load(f)
    return predict(sc, model)


@app.route("/predict_dt", methods=["POST"])
def predict_dt():
    with open("models/dt.pck", "rb") as f:
        sc, model = pickle.load(f)
    return predict(sc, model)


@app.route("/predict_knn", methods=["POST"])
def predict_knn():
    with open("models/knn.pck", "rb") as f:
        sc, model = pickle.load(f)
    return predict(sc, model)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

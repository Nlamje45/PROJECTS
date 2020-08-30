from flask import Flask, render_template, request,redirect,url_for
from flask_cors import CORS,cross_origin
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/',methods=['GET'])
@cross_origin()
def index():
    return render_template("index.html")

@app.route('/bulk')
#@cross_origin()
def bulk():
    return render_template("bulkpred.html")


@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()
def predict():
    model = pickle.load(open('model3.pkl', 'rb'))
    int_features = [int(x) for x in request.form.values()]
    final=[np.array(int_features, dtype=float)]
    prediction=model.predict(final)
    output=round(prediction[0],2)

    return render_template('index.html', predect_txt='The Rent of your house would be {} USD Only.'.format(output))

if __name__ == '__main__':
    app.run(debug=True)
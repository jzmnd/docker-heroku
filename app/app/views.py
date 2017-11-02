from app import app
from sklearn import datasets, svm
from flask import render_template, jsonify

# Load Dataset from scikit-learn
digits = datasets.load_digits()


@app.route('/')
def index():
    # Create SVM classifier
    clf = svm.SVC(gamma=0.001, C=100.)

    # Train
    clf.fit(digits.data[:-3], digits.target[:-3])

    # Predict
    prediction = clf.predict(digits.data[-3:])

    # Render html template
    html = render_template('index.html', prediction=jsonify({'value': repr(prediction)}))

    return html

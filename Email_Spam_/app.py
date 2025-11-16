from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']  # 👈 fixed here
    data = [message]
    transformed = vectorizer.transform(data)
    prediction = model.predict(transformed)[0]

    if prediction == 1:
        result = "This is a Spam message!"
    else:
        result = "This is a Safe (Ham) message."

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)

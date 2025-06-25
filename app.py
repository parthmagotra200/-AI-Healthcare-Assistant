from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Mock GPT-based symptom response
def get_symptom_response(symptom):
    responses = {
        "fever": "It might be a sign of viral infection. Please monitor your temperature and consider seeing a doctor.",
        "headache": "Could be due to stress or dehydration. Make sure to rest and drink water.",
        "cough": "Persistent coughs may need medical attention. If it's dry or severe, consult a physician."
    }
    return responses.get(symptom.lower(), "Sorry, I couldn't recognize that symptom. Please consult a medical professional.")

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        symptom = request.form.get("symptom")
        response = get_symptom_response(symptom)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
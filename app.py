from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for symptoms and diseases
SYMPTOMS_DB = {
    "fever": ["Influenza", "Dengue Fever", "Pneumonia", "Typhoid"],
    "chills": ["Jaundice", "Influenza", "Typhoid"],
    "itchy skin": ["Jaundice", "Eczema", "Chickenpox"],
    "weight loss": ["Jaundice", "Tuberculosis"],
    "yellow color inside the mouth": ["Jaundice"],
    "wheezing": ["Asthma"],
    "coughing": ["Asthma", "Tuberculosis", "Pneumonia"],
    "chest tightness": ["Asthma"],
    "shortness of breath": ["Asthma", "COVID-19", "Hypertension"],
    "persistent cough": ["Tuberculosis"],
    "chest pain": ["Tuberculosis", "Hypertension"],
    "night sweats": ["Tuberculosis"],
    "sore throat": ["Influenza", "Polio"],
    "fatigue": ["Influenza", "Typhoid"],
    "muscle pain": ["Influenza", "Malaria"],
    "sweating": ["Malaria", "Typhoid"],
    "nausea": ["Malaria", "Hepatitis", "Migraine", "Typhoid"],
    "vomiting": ["Malaria", "Migraine", "Typhoid"],
    "loss of taste or smell": ["COVID-19"],
    "difficulty breathing": ["COVID-19", "Pneumonia", "Hypertension"],
    "confusion": ["Alzheimer’s Disease", "Hypertension"],
    "mood swings": ["Alzheimer’s Disease"],
    "jaundice": ["Hepatitis"],
    "abdominal pain": ["Hepatitis", "Typhoid"],
    "dark urine": ["Hepatitis"],
    "severe headache": ["Dengue Fever", "Migraine", "Hypertension"],
    "skin rash": ["Dengue Fever", "Measles", "Chickenpox"],
    "bleeding": ["Dengue Fever"],
    "cough with phlegm": ["Pneumonia"],
    "paralysis": ["Polio"],
    "headache": ["Polio", "Typhoid"],
    "dizziness": ["Anemia", "Hypertension"],
    "pale skin": ["Anemia"],
    "weakness": ["Anemia", "Typhoid"],
    "aura (visual disturbances)": ["Migraine"],
    "red, dry, and itchy patches of skin": ["Eczema"],
    "red eyes": ["Measles", "Chickenpox"],
    "runny nose": ["Measles"],
    "stomach pain": ["Typhoid"],
    "loss of appetite": ["Typhoid"],
    "diarrhea": ["Cholera"],
    "dehydration": ["Cholera"],
    "muscle cramps": ["Cholera"],
    "low blood pressure": ["Cholera"],
    "itchy rash": ["Chickenpox"],
    "blisters": ["Chickenpox"],
    "blurred vision": ["Hypertension"]
}
@app.route("/")
def frontpg():
    return render_template("frontpg.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/details")
def details():
    return render_template("details.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/search", methods=["POST"])
def search():
    try:
        symptoms = request.json.get("symptoms", [])
        print("Received Symptoms:", symptoms)  # Debugging
        disease_matches = {}

        for symptom in symptoms:
            if symptom in SYMPTOMS_DB:
                for disease in SYMPTOMS_DB[symptom]:
                    if disease not in disease_matches:
                        disease_matches[disease] = []
                    disease_matches[disease].append(symptom)

        # Create a sorted list of diseases by the number of matching symptoms
        sorted_diseases = sorted(
            disease_matches.items(), 
            key=lambda x: len(x[1]), 
            reverse=True
        )

        print("Matched Diseases with Symptoms:", sorted_diseases)  # Debugging

        return jsonify({"diseases": sorted_diseases}), 200
    except Exception as e:
        print("Error occurred:", e)  # Debugging
        return jsonify({"error": "Something went wrong on the server."}), 500


if __name__ == "__main__":
    app.run(debug=True)

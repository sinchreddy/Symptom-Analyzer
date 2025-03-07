import mysql.connector

# Database connection configuration
db_config = {
    "host": "localhost",  # your MySQL host
    "user": "root",  # your MySQL username
    "password": "9008496759s",  # your MySQL password
    "database": "symptom_analyzer"  # your MySQL database name
}

def test_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Database connection successful!")
            connection.close()
        else:
            print("Database connection failed!")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

# Test connection
test_db_connection()




#const availableSymptoms = [
 #           "Fever", "Chills", "Itchy skin", "Weight loss", "Yellow color inside the mouth", 
 #           "Wheezing", "Coughing", "Chest tightness", "Shortness of breath", "Persistent cough", 
 #           "Chest pain", "Night sweats", "Sore throat", "Fatigue", "Muscle pain", "Sweating", 
 #           "Nausea", "Vomiting", "Loss of taste or smell", "Difficulty breathing", "Confusion", 
 #           "Mood swings", "Jaundice", "Abdominal pain", "Dark urine", "Severe headache", 
 #           "Skin rash", "Bleeding", "Cough with phlegm", "Paralysis", "Headache", "Dizziness", 
 #           "Pale skin", "Weakness", "Aura (visual disturbances)", "Red, dry, and itchy patches of skin", 
 #           "Red eyes", "Runny nose", "Stomach pain", "Loss of appetite", "Diarrhea", "Dehydration", 
 #           "Muscle cramps", "Low blood pressure", "Itchy rash", "Blisters", "Blurred vision"
 #       ];
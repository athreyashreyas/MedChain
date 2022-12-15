from flask import Flask, redirect, url_for, render_template, request
from ISP_Code import *
 
# Global Variables which are inputs from doctor and patient forms
patient_name = ""
patient_email = ""
patient_address = ""
patient_issue = ""
doctor_name = ""
doctor_email = ""
doctor_address = ""
doctor_specialization = ""
#doctor
#patient
 
 
app = Flask(__name__)
 
def home(): 
    return render_template("Patient.html")

@app.route("/patient", methods = ["POST", "GET"])
def get_patient_data():
    if request.method == "POST":
        global patient_address, patient_name, patient_email, patient_issue
        patient_name = request.form["name"]
        patient_email = request.form["email"]
        patient_address = request.form["address"]
        patient_issue = request.form["other"]
        #patient = Patient(patient_name, patient_email, )
        print(f"The patient's name is {patient_name}, their email is {patient_email}, address is {patient_address} and their issue is {patient_issue}")
    return render_template("Patient.html")


@app.route("/doctor", methods = ["POST", "GET"])
def get_doctor_data():
    if request.method == "POST":
        global doctor_address, doctor_name, doctor_email, doctor_specialization
        doctor_name = request.form["name"]
        doctor_email = request.form["email"]
        doctor_address = request.form["address"]
        doctor_specialization = request.form["specialization"]
        print(f"The doctor's name is {doctor_name}, their email is {doctor_email}, address is {doctor_address} and their specialization is {doctor_specialization}")
    return render_template("Doctor.html")

 
if __name__ == "__main__":
    app.run(debug = "True")
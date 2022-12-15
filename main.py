from flask import Flask, redirect, jsonify, url_for, render_template, request
from ISP_Code import *
from medchain import *
 
# Global Variables which are inputs from doctor and patient forms
patient_name = ""
patient_email = ""
patient_age = ""
patient_address = ""
patient_other = ""
patient_history = ""

doctor_name = ""
doctor_email = ""
doctor_address = ""
doctor_specialization = ""
doctor_hospital = ""

Medchain = None
doctor = None
patient = None
prescription = None

pres_req = False

 
 
app = Flask(__name__)
 
@app.route("/")
@app.route("/home")
def home(): 
    return render_template("Patient.html")

@app.route("/patient", methods = ["POST", "GET"])
def get_patient_data(pres = None):
    if request.method == "POST":
        global patient_address, patient_name, patient_age, patient_email, patient_other, patient, patient_history, doctor
        patient_name = request.form["name"]
        patient_email = request.form["email"]
        patient_age = request.form["age"]
        patient_address = request.form["address"]
        patient_other = request.form["other"]
        patient_history = request.form["history"]  #YE DEBUG KAROOO

        patient = Patient(patient_email, patient_name, patient_age, patient_address, patient_other, doctor.name)
        # patient.giveAccess(2) #keyD kya hai

        print(f"The patient's name is {patient_name}, their email is {patient_email}, age id {patient_age}, address is {patient_address} and their issue is {patient_other}, current doctor is {patient.currentDoctor}")

        return render_template("Patient.html")
    else: 
        return render_template("Patient.html", prescription = pres)

# @app.route("/patient_req_pres", methods = ["POST", "GET"])
# def req_pres():
#     if request.method == "POST":
#         global pres_req
#         pres_req = True
#     return render_template("Patient.html")

@app.route("/doctor", methods = ["POST", "GET"])
def get_doctor_data(hist = None):
    if request.method == "POST":
        global doctor_address, doctor_name, doctor_email, doctor_specialization, doctor_hospital, doctor
        doctor_name = request.form["name"]
        doctor_email = request.form["email"]
        doctor_address = request.form["address"]
        doctor_specialization = request.form["specialization"]
        doctor_hospital = request.form["hospital"]
        doctor = Doctor(doctor_email, doctor_name, doctor_address, doctor_hospital, doctor_specialization)

        print(f"The doctor's name is {doctor.name}, their email is {doctor_email}, address is {doctor_address}, hospital is {doctor_hospital} and their specialization is {doctor_specialization}")

        
    return render_template("Doctor.html", history = hist)

@app.route("/prescription", methods = ["POST", "GET"])
def get_prescription():
    global prescription, Medchain
    pres = request.form["prescription"]
    print(pres)
    prescription = Prescription(pres)
    Medchain = Blockchain()
    Medchain.add_pres(pres)
    print("Added the following prescription into the MedChain ledger: ")
    print(pres)
    return render_template("Patient.html", prescription = pres)

@app.route("/patienthistory",  methods = ["POST", "GET"])
def show_history():
    hist = "diarrhea"
    print(hist)
    return render_template("Doctor.html", history = hist)


@app.route("/chemist", methods = ["POST", "GET"])
def get_chemist():
    return render_template("Chemist.html")

@app.route("/about", methods = ["POST", "GET"])
def get_about():
    return render_template("About.html")

if __name__ == "__main__":
    app.run(debug = "True")
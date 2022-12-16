# MedChain

<h3>Project Description</h3>
A basic web application built to simulate interactions between a doctor, a patient and a pharmacist/chemist. All data transfer and flow of information between the three is cryptographically
secured using well known protocols and algorithms. The implementation of these algorithms is done using python and well known libraries. These functions are then linked to the frontend web-page using flask (a micro-web framework that allows the usage of python functions in js and html files).

<h3>Directory Structure</h3>
The files and folders are split as follows:
  
* <b>Templates (folder)</b> - Contains all the frontend HTML files, you have put all the HTML files in such a templates folder to run them on flask.
  
  * Chemist.html -> HTML file for the chemist page to deliver medicines to the patient based on the doctor's prescription.
  * Doctor.html -> HTML file for the doctor, who views the patient's history and can write prescription based on ailments. 
  * Patient.html -> HTML file for the patient, containing a form for the patient to fill their information and write their ailment/symptoms for the doctor to view. The application will send this information and the patient's history to the doctor.
  * About.html -> HTML file for the page containing the names and college IDs of all the people involved in this project.
 
* <b>ISP_Code.py </b> - A python file which contains all the code for the cryptographic algorithms, hashing functions and protocols (RSA, SHA-256, DHKE etc) used to secure and transfer the data.
* <b>main.py </b> - The main runner file which runs the web-application on a local machine/server. It contains the flask code linking all the functions and webpages together.

<h3>Steps to Run the Application </h3>
  
  
1. Install python and then flask on your local machine by running the following command on your terminal:
  
  
```
pip install flask 
```
2. Install other modules/libraries which you may not have in your machine. The ISP_Code.py file contains various cryptographic modules like Fernat, Hashlib etc. which you may not have on your machine/python version. Use the following pip command to install any package: 
  
```
pip install {name_of_package}
```
3. Run the following command on your terminal: 
  
```
python main.py
```
This should start a local server on your machine, ctrl + click on the host URL/path mentioned in the terminal or paste it on your browser's address bar to use the website.

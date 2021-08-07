# Emerging Technologies Project
# This is the python file for main home page

from flask import Flask, redirect, url_for, render_template, request
import os
from database_operations import mongodb_contactus_insert
import logging
import logging.handlers

import pymongo

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    check_logs("Home page is opened")
    return render_template("home.html")

@app.route("/managebooking")
#@app.route("/")
def managebooking():
    check_logs("Manage booking page is opened")
    return render_template("managebooking.html")

@app.route("/contactus")
#@app.route("/")
def contactus():
    check_logs("Contact Us page is opened")
    return render_template("contactus.html")

@app.route("/register")
#@app.route("/")
def register():
    check_logs("Register page is opened")
    return render_template("register.html")

@app.route("/login")
#@app.route("/")
def login():
    check_logs("Login page is opened")
    return render_template("login.html")

#http://127.0.0.1:5000/contactusdata
@app.route("/contactusdata", methods = ['POST'])
def contactus_data():
    from database_operations import mongodb_contactus_insert
    if request.method == "POST":
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        emailid = request.form.get('emailid')
        contact = request.form.get('contact')
        dob = request.form.get('dob')
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        subject = request.form.get('subject')

        result = '''
        <body bgcolor="lightblue">
        <h1>Data has been inserted!!</h1>
        <h1>Entered Information :</h1>
        <p>First Name : {}</p>
        <p>Last Name : {}</p>
        <p>Email ID : {}</p>
        <p>Contact : {}</p>
        <p>DOB : {}</p>
        <p>City : {}</p>
        <p>State : {}</p>
        <p>Country : {}</p>
        <p>Subject : {}</p>
        <h3>Please give us 24hours, our team would be surely get back to you!!</h3>
        <h3>Note: Hours of operation: Monday to Friday 10AM to 5PM</h3>
        </body>
        '''
        mongodb_contactus_insert(firstname, lastname, emailid, contact, dob, city, state, country, subject)
    return result.format(firstname, lastname, emailid, contact, dob, city, state, country, subject)

#http://127.0.0.1:5000/bookingdata
@app.route("/bookingdata", methods = ['POST'])
def booking_data():
    from database_operations import mongodb_booking_insert
    import uuid
    uid = uuid.uuid4()
    if request.method == "POST":
        countryFrom = request.form.get('countryFrom')
        countryTo = request.form.get('countryTo')
        departing = request.form.get('departing')
        returning = request.form.get('returning')

        result = '''
        <body bgcolor="lightblue">
        <h1>Your Booking has been done!!</h1>
        <h1>Your Booking Receipt :</h1>
        <p>Source : {}</p>
        <p>Destination : {}</p>
        <p>Departure : {}</p>
        <p>Returning : {}</p>
        <p>Booking Reference : {}</p>
        <h3>Please print your receipt!!</h3>
        </body>
        '''
        mongodb_booking_insert(countryFrom, countryTo, departing, returning, uid)
    return result.format(countryFrom, countryTo, departing, returning, uid)

#http://127.0.0.1:5000/contactusfilleddata
@app.route("/contactusfilleddata")
def contactus_filled_data():
    connection_string = "mongodb+srv://root:root@cluster0.dhp4w.mongodb.net/emerging_final_project?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["emerging_final_project"]
    cairlambton = db["airlambton"]
    columns = {"First_Name", "Last_Name", "Email_ID", "Contact_Number", "Date_Of_Birth", "City", "State", "Country", "Subject"}
    result = cairlambton.find({}, columns)
    fetched_first_name = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_last_name = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_email_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_contact_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_date_of_birth = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_city = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_country = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_subject = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    count = 0
    for row in result:
        fetched_first_name[i] = row['First_Name']
        fetched_last_name[i] = row['Last_Name']
        fetched_email_id[i] = row['Email_ID']
        fetched_contact_number[i] = row['Contact_Number']
        fetched_date_of_birth[i] = row['Date_Of_Birth']
        fetched_city[i] = row['City']
        fetched_state[i] = row['State']
        fetched_country[i] = row['Country']
        fetched_subject[i] = row['Subject']
        i = i + 1
        print(row)

    resultdisplay = '''
            <html lang="en">
            <head>
            <link rel="stylesheet" href="static/style.css">
            </head>
            <body bgcolor=#f7eaea>
            <div class="contactusdisplay">
                <hr/><hr/><h1>Hi Admin! Here is your data!!</h1><hr/><hr/>
                <h3>Contact Us Information :</h3><hr/>
                <h3>Query 1 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4>
                <hr/>
                <h3>Query 2 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4>
                <hr/>
                <h3>Query 3 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4>
                <hr/>
                <h3>Query 4 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4>
                <hr/>
                <h3>Query 5 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4>
                <hr/>
            </div>
            </body>
            </html>
                        '''
    return resultdisplay.format(fetched_first_name[0], fetched_last_name[0], fetched_email_id[0], fetched_contact_number[0], fetched_date_of_birth[0], fetched_city[0], fetched_state[0], fetched_country[0], fetched_subject[0],
                                fetched_first_name[1], fetched_last_name[1], fetched_email_id[1], fetched_contact_number[1], fetched_date_of_birth[1], fetched_city[1], fetched_state[1], fetched_country[1], fetched_subject[1],
                                fetched_first_name[2], fetched_last_name[2], fetched_email_id[2], fetched_contact_number[2], fetched_date_of_birth[2], fetched_city[2], fetched_state[2], fetched_country[2], fetched_subject[2],
                                fetched_first_name[3], fetched_last_name[3], fetched_email_id[3], fetched_contact_number[3], fetched_date_of_birth[3], fetched_city[3], fetched_state[3], fetched_country[3], fetched_subject[3],
                                fetched_first_name[4], fetched_last_name[4], fetched_email_id[4], fetched_contact_number[4], fetched_date_of_birth[4], fetched_city[4], fetched_state[4], fetched_country[4], fetched_subject[4])

#http://127.0.0.1:5000/contactusfilleddatadelete
@app.route("/contactusfilleddatadelete")
def contactus_filled_data_delete():
    connection_string = "mongodb+srv://root:root@cluster0.dhp4w.mongodb.net/emerging_final_project?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["emerging_final_project"]
    cairlambton = db["airlambton"]
    columns = {"First_Name", "Last_Name", "Email_ID", "Contact_Number", "Date_Of_Birth", "City", "State", "Country", "Subject"}
    result = cairlambton.find({}, columns)
    fetched_first_name = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_last_name = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_email_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_contact_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_date_of_birth = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_city = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_country = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_subject = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    count = 0
    for row in result:
        fetched_first_name[i] = row['First_Name']
        fetched_last_name[i] = row['Last_Name']
        fetched_email_id[i] = row['Email_ID']
        fetched_contact_number[i] = row['Contact_Number']
        fetched_date_of_birth[i] = row['Date_Of_Birth']
        fetched_city[i] = row['City']
        fetched_state[i] = row['State']
        fetched_country[i] = row['Country']
        fetched_subject[i] = row['Subject']
        i = i + 1
        print(row)

    resultdisplay = '''
            <html lang="en">
            <head>
            <link rel="stylesheet" href="static/style.css">
            </head>
            <body bgcolor=#f7eaea>
            <div class="contactusdisplay">
            <form action="http://127.0.0.1:5000/deleteOne">
                <hr/><hr/><h1>Hi Admin! Here is your data!! Click on Button to Delete the Data</h1><hr/><hr/>
                <h3>Contact Us Information :</h3><hr/>
                <h3>Query 1 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4>
                <input type="submit" value="Delete Entry">
                <hr/>
                <h3>Query 2 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4>
                <input type="submit" value="Delete Entry">
                <hr/>
                <h3>Query 3 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4>
                <input type="submit" value="Delete Entry">
                <hr/>
                <h3>Query 4 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4>
                <input type="submit" value="Delete Entry">
                <hr/>
                <h3>Query 5 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4>
                <input type="submit" value="Delete Entry">
                <hr/>
            </form>
            </div>
            </body>
            </html>
                        '''
    return resultdisplay.format(fetched_first_name[0], fetched_last_name[0], fetched_email_id[0], fetched_contact_number[0], fetched_date_of_birth[0], fetched_city[0], fetched_state[0], fetched_country[0], fetched_subject[0],
                                fetched_first_name[1], fetched_last_name[1], fetched_email_id[1], fetched_contact_number[1], fetched_date_of_birth[1], fetched_city[1], fetched_state[1], fetched_country[1], fetched_subject[1],
                                fetched_first_name[2], fetched_last_name[2], fetched_email_id[2], fetched_contact_number[2], fetched_date_of_birth[2], fetched_city[2], fetched_state[2], fetched_country[2], fetched_subject[2],
                                fetched_first_name[3], fetched_last_name[3], fetched_email_id[3], fetched_contact_number[3], fetched_date_of_birth[3], fetched_city[3], fetched_state[3], fetched_country[3], fetched_subject[3],
                                fetched_first_name[4], fetched_last_name[4], fetched_email_id[4], fetched_contact_number[4], fetched_date_of_birth[4], fetched_city[4], fetched_state[4], fetched_country[4], fetched_subject[4])

#http://127.0.0.1:5000/deleteOne
@app.route("/deleteOne")
def contactus_filled_data_delete1():
    connection_string = "mongodb+srv://root:root@cluster0.dhp4w.mongodb.net/emerging_final_project?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["emerging_final_project"]
    cairlambton = db["airlambton"]
    cairlambton.delete_one({})
    return render_template("admin.html")

#http://127.0.0.1:5000/managebookingdata
@app.route("/managebookingdata")
def managebookingdata():
    connection_string = "mongodb+srv://root:root@cluster0.dhp4w.mongodb.net/emerging_final_project?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["emerging_final_project"]
    cairlambtonmanage = db["airlambtonbooking"]
    columns = {"Source", "Destination", "Departure", "Return", "BookingReference"}
    result = cairlambtonmanage.find({}, columns)
    fetched_countryFrom = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_countryTo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_departing = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_returning = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_uid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    count = 0
    for row in result:
        fetched_countryFrom[i] = row['Source']
        fetched_countryTo[i] = row['Destination']
        fetched_departing[i] = row['Departure']
        fetched_returning[i] = row['Return']
        fetched_uid[i] = row['BookingReference']
        i = i + 1
        print(row)

    resultdisplay = '''
            <html lang="en">
            <head>
            <link rel="stylesheet" href="static/style.css">
            </head>
            <body bgcolor=#f7eaea>
            <div class="contactusdisplay">
                <hr/><hr/><h1>Hi! Here is your booking details!!</h1><hr/><hr/>
                <h3>Booking Information :</h3><hr/>
                <h4>Country From : {} <br/> Country To : {} <br/> Departing : {} <br/> Returning : {} <br/> Booking Reference : {} <br/>
                <hr/>
                <h3>Please call us on +1-905-999-0011 to change/cancel/reschedule your booking</h3><hr/>
            </div>
            </body>
            </html>
                        '''
    return resultdisplay.format(fetched_countryFrom[0], fetched_countryTo[0], fetched_departing[0], fetched_returning[0], fetched_uid[0])

@app.route("/faq")
#@app.route("/")
def faq():
    check_logs("FAQ page is opened")
    return render_template("faq.html")

@app.route("/covidupdate")
#@app.route("/")
def covidupdate():
    check_logs("Covid update page is opened")
    return render_template("covidupdate.html")

@app.route("/luggage")
#@app.route("/")
def luggage():
    check_logs("Luggage page is opened")
    return render_template("luggage.html")

@app.route("/admin")
#@app.route("/")
def admin():
    check_logs("Admin page is opened")
    return render_template("admin.html")

def check_logs(message):
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()
    fhandler = logging.FileHandler(filename='websitelog.log', mode='a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    logger.setLevel(logging.DEBUG)
    logger.debug(message)

if __name__ == "__main__":
    app.run()
    #connect_to_mongodb()


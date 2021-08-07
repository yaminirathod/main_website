from flask import Flask, redirect, url_for, render_template, request
import os

import pymongo

def mongodb_contactus_insert(firstname, lastname, emailid, contact, dob, city, state, country, subject):
    connection_string = "mongodb+srv://root:root@cluster0.dhp4w.mongodb.net/emerging_final_project?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["emerging_final_project"]
    cairlambton = db["airlambton"]
    # Insert Record
    mydict = {"First_Name": firstname, "Last_Name": lastname, "Email_ID": emailid, "Contact_Number": contact,
              "Date_Of_Birth": dob, "City": city, "State": state, "Country": country, "Subject": subject}
    x = cairlambton.insert_one(mydict)
    print(x)
    

def mongodb_booking_insert(countryFrom, countryTo, departing, returning, uid):
    connection_string = "mongodb+srv://root:root@cluster0.dhp4w.mongodb.net/emerging_final_project?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["emerging_final_project"]
    cairlambtonbooking = db["airlambtonbooking"]
    # Insert Record
    mydict = {"Source": countryFrom, "Destination": countryTo, "Departure": departing, "Return": returning, "BookingReference": uid}
    x = cairlambtonbooking.insert_one(mydict)
    print(x)

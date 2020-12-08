import mysql.connector
import pandas as pd
import requests
from io import StringIO

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="LiteEx"
)
mycursor = mydb.cursor()
#mycursor.execute('create database IF NOT EXISTS LiteEx')
    # customerid | firstname | lastname | companyname | billingaddress1 | billingaddress2 | city | state | postalcode | country | phonenumber | emailaddress | createddate
sql = '''CREATE TABLE IF NOT EXISTS tbl_customer(
    customerid INT AUTO_INCREMENT PRIMARY KEY, 
    firstname VARCHAR(15), 
    lastname VARCHAR(15), 
    companyname VARCHAR(255), 
    billingaddress1 TEXT, 
    billingaddress2 TEXT, 
    city VARCHAR(255), 
    state VARCHAR(5), 
    postalcode VARCHAR(20) , 
    country VARCHAR(50), 
    phonenumber VARCHAR(12), 
    emailaddress VARCHAR(50), 
    createddate VARCHAR(50))'''
mycursor.execute(sql)


link = 'https://drive.google.com/file/d/1VWBNNsFk-kM0cTkEWZG8cSjEfiAeESSn/view'
dwn_url = 'https://drive.google.com/uc?export=download&id=' + \
    link.split('/')[-2]

df = pd.read_csv(dwn_url)

for itm in df.index:
    # customerid | firstname | lastname | companyname | billingaddress1 | billingaddress2 | city | state | postalcode | country | phonenumber | emailaddress | createddate
    mycursor = mydb.cursor()
    sql = "insert ignore into tbl_customer(customerid, firstname, lastname, companyname, billingaddress1, billingaddress2, city, state, postalcode, country, phonenumber, emailaddress, createddate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (str(df['customerid'][itm]), str(df['firstname'][itm]), str(df['lastname'][itm]), str(df['companyname'][itm]), str(df['billingaddress1'][itm]), str(df['billingaddress2'][itm]), str(
        df['city'][itm]), str(df['state'][itm]), str(df['postalcode'][itm]), str(df['country'][itm]), str(df['phonenumber'][itm]), str(df['emailaddress'][itm]), str(df['createddate'][itm]))
    mycursor.execute(sql, val)
    print('inserted customerid: ', df['customerid'][itm])
    mydb.commit()

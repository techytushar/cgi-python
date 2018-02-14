#!/usr/bin/python3.5

import cgi
import sqlite3
c=0
print("Content-Type:text/html\n\n")
data = cgi.FieldStorage()
#getting the values from the register page.
name = data.getvalue("name")
username = data.getvalue("username")
email = data.getvalue("email")
gender = data.getvalue("gender")
contact = data.getvalue("contact")
password = data.getvalue("password")

if(name and username and email and gender and contact and password):
    try:
        #setting up the database connection and storing the values.
        con = sqlite3.connect("/var/www/python workshop/workshop.db")
        cur = con.cursor()
        cur.execute('select * from users where username = "'+username+'"')
        data = cur.fetchall()
        if(data):
            #fail
            c=2
        else:
            cur.execute('insert into users ("name","username","email","gender","contact","password") values("'+str(name)+'", "'+str(username)+'", "'+str(email)+'", "'+str(gender)+'", "'+str(contact)+'", "'+str(password)+'")')
            con.commit()
            #success
            c=1
    except:
        #database problem
        c=4
    finally:
        con.close()

else:
    #incomplete
    c=3

def success():
    print("""
    <html>
        <head>
            <title>Success!</title>
            <style>
                body{
                    font-family:Helvetica,sans-serif;
                    padding: 0 20px;
                }
            </style>
        </head>
        <body>
            <h3>"""+str(username+" is successfully registered!")+"""</h3>
            <h3><a href="login.py">Login Here</a></h3>
        </body>
    </html>""")

def fail():
    print("""
    <script>
        window.location="register.py?message=fail";
    </script>
    """)
    print

def incomplete():
    print("""
    <script>
        window.location="register.py?message=incomplete";
    </script>
    """)
    print
    
def databaseProblem():
    print("""
    <html>
        <head>
            <title>Oops!!</title>
            <style>
            body{
                font-family:Helvetica,sans-serif;
                padding: 0 20px;
            }
            </style>
        </head>
        <body>
            <h3 style="color:red;">Error occured while writting to the database, please try again!</h3>
            <h3><a href="main.py">Register Here</a></h3>
        </body>
    </html>
    """)

if(c==1):
    success()
elif(c==2):
    fail()
elif(c==3):
    incomplete()
elif(c==4):
    databaseProblem()

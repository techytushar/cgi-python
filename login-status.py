#!/usr/bin/python3.5

import cgi
import sqlite3

print("Content-Type:text/html\n\n")

try:
    data = cgi.FieldStorage()
    username = data.getvalue("username")
    password = data.getvalue("password")
except:
    username,password = "",""
check = 0

if(username and password):
    con = sqlite3.connect("workshop.db")
    cur = con.cursor()
    cur.execute("select * from users where username = '"+username+"'")
    temp = cur.fetchone()
    if(temp and temp[6]==password):
        #success
        c=1
    else:
        #username error
        c=2
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
            <h3>"""+str("Welcome "+temp[1])+"""</h3>
            <h3>Redirecting, Please Wait!</h3>
        </body>
        <script>
            setInterval(function(){
                window.location = "index.html"
            },2000)
        </script>
    </html>""")
    print

def fail():
    print("""
    <html>
    <script>
        window.location="login.py?message=fail";
    </script>
    </html>
    """)
    print

def incomplete():
    print("""
    <html>
    <script>
        window.location="login.py?message=incomplete";
    </script>
    </html>
    """)
    print

if c==1:
    success()
elif(c==2):
    fail()
elif(c==3):
    incomplete()

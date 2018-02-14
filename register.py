#!/usr/bin/python3.5

import cgi
data = cgi.FieldStorage()
status = data.getvalue("message")

print("Content-Type:text/html\n\n")

if(status=="incomplete"):
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Form</title>
        <style>
            body{
                font-family:Helvetica,sans-serif;
                padding: 0 20px;
            }
            h3{
                color:red;
            }
        </style>
    </head>
    <body>
        <h1>Registration Form:</h1>
        <h3>"""+str("Please fill all the fields and try again.")+"""</h3>
        <form action = "result.py" action="post">
            <span>Name: <input type = "text" name = "name" autocomplete="off"></span><br><br>
            <span>Username: <input type = "text" name = "username" autocomplete="off"></span><br><br>
            <span>E-mail: <input type = "email" name="email" autocomplete="off"></span><br><br>
            <span>Gender: 
                Male <input type="radio" name="gender" value="male"> 
                Female <input type="radio" name="gender" value="male"></span><br><br>
            <span>Contact: <input type = "text" name="contact" autocomplete="off"></span><br><br>
            <span>Password: <input type="password" name="password" autocomplete="off"></span><br><br>
            <span><input type="submit" value="Submit !"></span>
        </form>
    </body>
    </html>
    """)

elif(status=="fail"):
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Form</title>
        <style>
            body{
                font-family:Helvetica,sans-serif;
                padding: 0 20px;
            }
            h3{
                color:red;
            }
        </style>
    </head>
    <body>
        <h1>Registration Form:</h1>
        <h3>"""+str("Username already in use")+"""</h3>
        <form action = "result.py" action="post">
            <span>Name: <input type = "text" name = "name" autocomplete="off"></span><br><br>
            <span>Username: <input type = "text" name = "username" autocomplete="off"></span><br><br>
            <span>E-mail: <input type = "email" name="email" autocomplete="off"></span><br><br>
            <span>Gender: 
                Male <input type="radio" name="gender" value="male"> 
                Female <input type="radio" name="gender" value="male"></span><br><br>
            <span>Contact: <input type = "text" name="contact" autocomplete="off"></span><br><br>
            <span>Password: <input type="password" name="password" autocomplete="off"></span><br><br>
            <span><input type="submit" value="Submit !"></span>
        </form>
    </body>
    </html>
    """)
    
else:
    print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Form</title>
    <style>
        body{
            font-family:Helvetica,sans-serif;
            padding: 0 20px;
        }
    </style>
</head>
<body>
    <h1>Registration Form:</h1>
    <form action = "result.py" action="post">
        <span>Name: <input type = "text" name = "name" autocomplete="off"></span><br><br>
        <span>Username: <input type = "text" name = "username" autocomplete="off"></span><br><br>
        <span>E-mail: <input type = "email" name="email" autocomplete="off"></span><br><br>
        <span>Gender: 
            Male <input type="radio" name="gender" value="male"> 
            Female <input type="radio" name="gender" value="male"></span><br><br>
        <span>Contact: <input type = "text" name="contact" autocomplete="off"></span><br><br>
        <span>Password: <input type="password" name="password" autocomplete="off"></span><br><br>
        <span><input type="submit" value="Submit !"></span>
    </form>
</body>
</html>
""")
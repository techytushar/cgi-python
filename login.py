#!/usr/bin/python3.5

import cgi

print("Content-Type:text/html\n\n")

data = cgi.FieldStorage()
status = data.getvalue("message")

def error(status):
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
    <h1>Login Here:</h1>
    <h3>"""+status+"""</h3>
    <form action = "login-status.py" method="post">
        <span>Username: <input type = "text" name = "username" autocomplete="off"></span><br><br>
        <span>Password: <input type="password" name="password" autocomplete="off"></span><br><br>
        <span><input type="submit" value="Submit !"></span>
    </form>
</body>
</html>
""")

if(status):
    if(status=="incomplete"):
        error("Please fill all the fields and try again.")
    elif(status=="fail"):
        error("Incorrect username or password")

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
            h3{
                color:red;
            }
        </style>
    </head>
    <body>
        <h1>Login Here:</h1>
        <form action = "login-status.py" method="post">
            <span>Username: <input type = "text" name = "username" autocomplete="off"></span><br><br>
            <span>Password: <input type="password" name="password" autocomplete="off"></span><br><br>
            <span><input type="submit" value="Submit !"></span>
        </form>
    </body>
    </html>
    """)



import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("News2Mail_API_user")
    password = os.getenv("News2Mail_API")

    receiver = "SomeMail@post.bgu.ac.il"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        print("email sent!")

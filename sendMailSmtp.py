# send Mail using SMTP

import smtplib
from email.mime.text import MIMEText


import requests
import json
import os
url = 'http://awz66661.icu:8000/defaultemail'
key = os.environ.get("APIAUTH")
print(key)
params = {
    "key": key
}

response = requests.get(url, params=params)
defaultemail = json.loads(response.text)
sender_pass = defaultemail["sender_pass"]
smtp_server = defaultemail["smtp_server"]
smtp_port = defaultemail["smtp_port"]
sender = defaultemail["sender"]
rec = defaultemail["rec"]


def send_mail(subject, content, rec=rec, sender=sender, sender_pass=sender_pass, smtp_server=smtp_server, smtp_port=smtp_port, if_html=False):

    msg = MIMEText(content, 'html' if if_html else 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = rec
    try:
        s = smtplib.SMTP_SSL(smtp_server, smtp_port)
        s.login(sender, sender_pass)
        s.sendmail(sender, rec, msg.as_string())
        print("Send mail successfully")
    except smtplib.SMTPException as e:
        print("Error: Send mail failed")
        print(e)
    finally:
        s.quit()



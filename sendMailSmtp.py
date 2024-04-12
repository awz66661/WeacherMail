# send Mail using SMTP

import smtplib
from email.mime.text import MIMEText


def send_mail(subject, content):
    sender_pass = "tvioqkdxauxgecea"
    smtp_server = "smtp.qq.com"
    smtp_port = 465
    sender = "2362422778@qq.com"
    rec = "21307130326@m.fudan.edu.cn"
    msg = MIMEText(content)
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



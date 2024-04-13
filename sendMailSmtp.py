# send Mail using SMTP

import smtplib
from email.mime.text import MIMEText


sender_pass = "tvioqkdxauxgecea"
smtp_server = "smtp.qq.com"
smtp_port = 465
sender = "2362422778@qq.com"
rec = "21307130326@m.fudan.edu.cn"

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



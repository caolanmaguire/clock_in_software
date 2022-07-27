import smtplib
import imghdr
from email.message import EmailMessage
from datetime import date
import os

email_footer_file = '\n\n</Smart Clocker>'
email_intro_file = '<Smart Clocker>\n Welcome to smart clocker!' 
email_subject_file = 'Smart Clocker | Automated Email' 

email_footer = email_footer_file
email_intro = email_intro_file
email_subject = email_subject_file

def send_email(reciever_email, email_msg):
    sender_email = "combitelematicsreport@gmail.com"
    password = 'dtaoxkwbografkya'

    new_message = EmailMessage()
    new_message['Subject'] = email_intro
    new_message['From'] = sender_email
    new_message['To'] = reciever_email
    new_message.set_content((email_msg + '\n\n' + email_footer))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(sender_email, password)              
        smtp.send_message(new_message)
send_email('caolanmichaelmaguire@gmail.com', 'This is the email message')
print(email_footer_file)
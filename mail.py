import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import pandas as pd

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Environment Variables
SMTP_URL = os.environ.get("SMTP_URL")
PORT = os.environ.get("PORT")
SENDER_NAME = os.environ.get("SENDER_NAME")
SENDER = os.environ.get("SENDER")
PASSWORD = os.environ.get("PASSWORD")

df = pd.read_csv('list.csv')   # Read CSV file
products_list = df.values.tolist()
receiver_list = [] # List of Email Address of Receivers
name_list = []     # Name of receivers.
for i in products_list:
    receiver_list.append(i[1])
    name_list.append(i[0])

#to send emails
def send_mail(i):    
    msg = MIMEMultipart()       # instance of MIMEMultipart   
    msg['From'] = f"{SENDER_NAME}  {SENDER}"        # storing the senders email address   
    msg['To'] = receiver_list[i]         # storing the receivers email address  
    # print(receiver_list[i])
    msg['Subject'] = "Hello WOrld" # storing the subject  
    # string to store the body of the mail 
    body = f''' 
    # Mail body here. 
    # Variables can be accessed here for e.g. 
    Hi {name_list[i]},
    
    This is a test mail.
    
    Regards,
    Smit
    
    '''
    msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
    pdf_name = 'test.pdf'
    # pdf_name = f'{name_list[i]}_{i}.pdf'        # open the file to be sent  
    filename = pdf_name
    attachment = open(filename, "rb") 
    p = MIMEBase('application', 'octet-stream')      # instance of MIMEBase and named as p 
    p.set_payload((attachment).read())       # To change the payload into encoded form 
    encoders.encode_base64(p)       # encode into base64  
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p)   # attach the instance 'p' to instance 'msg' 
    s = smtplib.SMTP(SMTP_URL, PORT)  # creates SMTP session 
    s.starttls() # start TLS for security
    s.login(SENDER,PASSWORD)  # Authentication 
    text = msg.as_string() # Converts the Multipart msg into a string 
    s.sendmail(SENDER, receiver_list[i], text)  # sending the mail 
    print(f'{i+1} ==> Mail sent to {name_list[i]} ==> {receiver_list[i]}')
    s.quit() # terminating the session 


def rename_pdf():
    '''Rename pdf file. '''
    os.chdir('C:\\Users\\HP\\Documents\\Python Scripts\\mail\\data')
    i=0
    for file in os.listdir():
        src = file
        dst = f'{name_list[i]}_{i}.pdf'
        os.rename(src,dst)
        print(f'File renamed with {dst}')
        i+=1

# rename_pdf()  # Call this function if you wants to change pdf name.

for i in range(len(receiver_list)):
    send_mail(i)

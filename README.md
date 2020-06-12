# mail-script
Automate your mails with Python


*Python code to illustrate Sending mail with attachments from your Gmail account*

**Libraries to be imported**
- smtplib 
- from email.mime.multipart import MIMEMultipart 
- from email.mime.text import MIMEText 
- from email.mime.base import MIMEBase 
- from email import encoders 
- pandas


Note: Turn off "Less secure app access" [Click here](https://support.google.com/accounts/answer/6010255?hl=en)

#Scenario:
We had organized Webinar Series and received more than 500 registrations. Now the challenge was to send certificate to them. 
To tackle this problem, I wrote this small python script in Python. Script takes input as a [CSV](/list.csv) and send mail to participants with individual certificate in PDF. 

I have also mentioned rename_pdf function in the script, it changes the certificate name to 'username_int' to make each and every file unique. So It will be easy to send mail with the attachment.

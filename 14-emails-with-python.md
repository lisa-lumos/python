# Emails with Python
Send emails with Python and check inbox for received messages. This process is highly reliant on admin privileges on both your local computer, your network, and your email. It is highly likely that on a corporate network, work computer, or work email, these methods will be blocked for security reasons. 

Each major email provider has their own SMTP (Simple Mail Transfer Protocol) Server. For example, gmail has `smtp.gmail.com`, outlook has `smtp-mail.outlook.com`, etc. Which is a a domain name you connect to, to access your emails programmatically. 

For gmail users, you need to generate an app password (not your normal pwd) just for your python script. `https://myaccount.google.com/apppasswords` to generate app passwords. Select app: Mail, Select device: Python connection. (customized name)

## Send emails
```py
import smtplib
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo() # greets the server, need to be immediately after obj creation
smtp_obj.starttls() # initiate TLS encryption
import getpass
email = getpass.getpass("Email: ") # will hide your input
pwd = getpass.getpass("App Password: ") 
smtp_obj.login(email, pwd)
from_address = email
to_address = email
subject =  "This is my subject"
message = "This is my message"
msg = "Subject: " + subject + '\n' + message # construct the email text
smtp_obj.sendmail(from_address, to_address, msg)
smtp_obj.quit() # close the connection
```

## Receive emails
```py
import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
import getpass
email = getpass.getpass("Email: ")
pwd = getpass.getpass("App Password: ") 
M.login(email, pwd)
M.list() # shows everything you can check in your email
M.select('inbox')
my_type, my_ids = M.search(None, 'SUBJECT "This is my subject"')
id1 = my_ids[0] # the id of the first email in the search result
print(id1)
result, email_data = M.fetch(id1, '(RFC822)')
print(email_data) # all sorts of info, including email subject and content
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
import email # parses the raw_email_string
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body) # b'This is my message\r\n'
M.close()
```















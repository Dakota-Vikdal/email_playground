import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Establish a connection between this file and the html file.
html = Template(Path('index.html').read_text())

# Create the basic email components such as who the email is from, who it is going to and
# the subject of the email
email = EmailMessage()
email['from'] = 'Nat the Bat'
email['to'] = 'yogadaddy666@gmail.com'
email['subject'] = 'I am the coolest arent I!! THE COSMOS FLOW THROUGH ME LIKE A TURD FLOWS THROUGH YOU!'

# Utilize the dynamic aspect of the html file. In this case, name.
email.set_content(html.substitute({'name': '!NatAttack!'}), 'html')

# Establish the email that will be sending this email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('natdoe4@gmail.com', 'ldvc mesb emsn mbux')
    smtp.send_message(email)
    print('all good boss!')
        

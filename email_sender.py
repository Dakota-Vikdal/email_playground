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
email['to'] = 'example1996@hotmail.com'
email['subject'] = 'Am I cool or what?!'

# Utilize the dynamic aspect of the html file. In this case, name.
email.set_content(html.substitute({'name': '!NatAttack!'}), 'html')

# Establish the email that will be sending this email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('example@gmail.com', 'ldvc mesb emsn mbux')
    smtp.send_message(email)
    print('all good boss!')
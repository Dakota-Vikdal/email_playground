import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Nat the Bat'
email['to'] = 'yogadaddy666@gmail.com'
email['subject'] = 'I am the coolest arent I!! THE COSMOS FLOW THROUGH ME LIKE A TURD FLOWS THROUGH YOU!'

email.set_content(html.substitute({'name': '!NatAttack!'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('natdoe4@gmail.com', 'ldvc mesb emsn mbux')
    smtp.send_message(email)
    print('all good boss!')
        

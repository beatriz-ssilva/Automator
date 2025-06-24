import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def send_email():
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    EMAIL_TO = os.getenv("EMAIL_TO")

    msg = EmailMessage()
    msg['Subject'] = 'Arquivo baixado automaticamente'
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO
    msg.set_content('Segue em anexo o arquivo baixado.')

    filename = os.listdir("downloads")[0]
    filepath = os.path.join("downloads", filename)

    with open(filepath, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=filename)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)

    print(f"E-mail enviado para {EMAIL_TO} com anexo {filename}.")

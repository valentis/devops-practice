from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_email(to: str, subject: str, html_body: str, config: dict):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = config["SMTP_USER"]
    msg["To"] = to
    msg.attach(MIMEText(html_body, "html"))
    with smtplib.SMTP(config["SMTP_HOST"], config["SMTP_PORT"]) as server:
        server.starttls()
        server.login(config["SMTP_USER"], config["SMTP_PASS"])
        server.send_message(msg)

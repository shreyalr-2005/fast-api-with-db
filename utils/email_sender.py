import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()
app_password=os.getenv("APP_PASSWORD")
sender_email=os.getenv("SENDER_EMAIL")

# Create email
def send_email(receiver_email: str, subject: str, content: str):
    """Send an email to the given receiver with the specified subject and content."""
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(content)

# Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        # server.starttls()          # Secure connection
        server.login(sender_email, app_password)
        server.send_message(msg)

    return f"Email sent successfully to {receiver_email}"
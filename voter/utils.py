import smtplib
import email
import os

# Create a SMTP connection to Gmail
smtp_server = 'smtp.gmail.com'
port = 587
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")

def send_otp_mail(otp, receiver_mail):
    print(os.getenv("USER_NAME"))
    print(os.getenv("PASSWORD"))
    # Create an email message
    message = email.message_from_string(f'your otp : {otp}')
    message['From'] = 'sarwatm225@gmail.com'
    message['To'] = receiver_mail
    message['Subject'] = 'Voting Confirmation'

    # Send the email message
    smtp_client = smtplib.SMTP(smtp_server, port)
    smtp_client.ehlo()
    smtp_client.starttls()
    smtp_client.login(username, password)
    smtp_client.sendmail(message['From'], message['To'], message.as_string())
    smtp_client.quit()

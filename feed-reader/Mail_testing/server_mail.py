import getpass
import smtplib
import os

def send_email(subject, message):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    # Get email credentials from environment variables
    FROM_EMAIL = os.environ.get("tobiasprogramming@outlook.com")  # Use the correct environment variable name
    PASSWORD = os.environ.get("Software2005")  # Use the correct environment variable name
    TO_EMAIL = "tobiasvdvaart@gmail.com"

    # Check if credentials are available
    if FROM_EMAIL is None or PASSWORD is None:
        print("Email credentials not found in environment variables.")
        return


    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Login {status_code} {response}")

    message_body = f"Subject: {subject}\n\n{message}"

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, message_body)
    smtp.quit()

if __name__ == "__main__":
    subject = "Mail sent using Python"
    message = """Hi there,

This is a test email sent using a Python function.

Thanks,
Test account
"""

    send_email(subject, message)

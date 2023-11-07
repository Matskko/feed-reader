import getpass
import smtplib

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "tobiasprogramming@outlook.com"  
TO_EMAIL = "tobiasvdvaart@gmail.com"
PASSWORD = getpass.getpass("Enter password:")

MESSAGE = """Subject: mail sent using python
hi test,

this is a test e-mail
thanks,
test account
"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Login {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()

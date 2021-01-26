import requests # pip install requests
import csv
import time

source_file = "emails.csv" # Change filename/path according to yours
destination_file = "valid_emails.csv" # Change filename/path according to yours (if not then it will create don't worry)

with open(source_file, 'r') as emails_data:
    emails = csv.reader(emails_data)
    for email in emails:
        response = requests.get("https://isitarealemail.com/api/email/validate", params={'email':email})
        status = response.json()['status']
        time.sleep(2)
        if status == "valid":
            with open(destination_file, 'a', newline="") as valid_emails:
                valid_email = csv.writer(valid_emails)
                valid_email.writerow(email)
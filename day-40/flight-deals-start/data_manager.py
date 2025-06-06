import os
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv
import smtplib

load_dotenv()
SHEETY_ENDPOINT = os.getenv("GOOGLE_SHEET_URL")#Google sheet endpoint
GOOGLE_SHEET_USER_LIST_URL = os.getenv("GOOGLE_SHEET_USER_LIST_URL")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.password = os.getenv("PW")
        self.username = os.getenv("USERNAME")
        self.auth = (self.username, self.password)
        self.destination_data = {}
        self.user_email = []
        self.my_email = os.getenv("MY_EMAIL")
        self.my_password = os.getenv("EMAIL_PW")

    def get_sheet_data(self):
        sheet_response = requests.get(url=SHEETY_ENDPOINT, auth=self.auth)
        data = sheet_response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_code(self):
        for row in self.destination_data:
            row_id = row["id"]
            update_data = {
                "price":{
                    "iataCode": row["iataCode"]
                }
            }
            update_url = f"{SHEETY_ENDPOINT}/{row_id}"
            update_iata = requests.put(url=update_url, json=update_data, auth=self.auth)


    def update_iata_code(self, iata_code, id):
        update_data = {
            "price": {
                "iataCode": iata_code
            }
        }
        update_url = f"{SHEETY_ENDPOINT}/{id}"

        try:
            update_iata = requests.put(url=update_url, json=update_data, auth=self.auth)
            if update_iata.status_code == 200:
                print(f"Successfully updated IATA code for row {id}")
            else:
                print(f"Error updating IATA code for row {id}: {update_iata.status_code}")
                print(update_iata.text)  # Log the response text to understand the error
        except Exception as e:
            print(f"Exception occurred while updating IATA code: {e}")

    def get_user_email(self):
        response = requests.get(url=GOOGLE_SHEET_USER_LIST_URL, auth=self.auth)
        user_list_data = response.json()
        # print(user_list_data)
        for email in user_list_data["userList"]:
            user_email = email["emailAddress"]
            self.user_email.append(user_email)
        # print(self.user_email)
        return self.user_email

    def send_email(self, email, message):
        try:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.my_password)
                connection.sendmail(from_addr=self.my_email, to_addrs=email,
                                    msg=f"Subject: Flights data!\n\n {message}")
                print(f"Email sent successfully to {email}")
        except Exception as error_message:
            print(f"Oops: {error_message}")






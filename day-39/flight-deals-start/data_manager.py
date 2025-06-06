import os
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
SHEETY_ENDPOINT = os.getenv("GOOGLE_SHEET_URL")#Google sheet endpoint


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.password = os.getenv("PW")
        self.username = os.getenv("USERNAME")
        self.auth = (self.username, self.password)
        self.destination_data = {}

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





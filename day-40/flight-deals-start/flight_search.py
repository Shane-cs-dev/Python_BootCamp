import requests
import os
from dotenv import load_dotenv


load_dotenv()
AMADEUS_URL_TOKEN = os.getenv("AMADEUS_URL_TOKEN")
AMADEUS_IATA_SEARCH = os.getenv("AMADEUS_IATA_SEARCH")
AMADEUS_PRICE_SEARCH = os.getenv("AMADEUS_PRICE_SEARCH")
GRANT_TYPE = "client_credentials"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")
        self.token = {}

    def get_amadeus_token(self):
        token_data = {
            "grant_type": GRANT_TYPE,
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        self.token = requests.post(url=AMADEUS_URL_TOKEN, data=token_data)
        access_token = self.token.json()["access_token"]
        return access_token

    def destination_code(self, city_name):
        headers = {
            "Authorization": f"Bearer {self.get_amadeus_token()}"
        }
        iata_params = {
            "keyword": city_name
        }
        iata_response = requests.get(url=AMADEUS_IATA_SEARCH, headers=headers, params=iata_params)
        city_code = iata_response.json()["data"][0]["iataCode"]
        # print(city_code)
        return city_code

    def check_flight(self, departure_airport, arrival_airport, departure_date, return_date, is_direct=True):
        headers = {
            "Authorization": f"Bearer {self.get_amadeus_token()}"
        }
        flight_params = {
            "originLocationCode": departure_airport,
            "destinationLocationCode": arrival_airport,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "TWD",
            "max": "20"
        }
        flight_response = requests.get(url=AMADEUS_PRICE_SEARCH, headers=headers, params=flight_params)
        # print(flight_response.json())
        return flight_response.json()





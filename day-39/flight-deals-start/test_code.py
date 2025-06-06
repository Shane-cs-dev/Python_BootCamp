#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pprint import pprint
#Sheety API
GOOGLE_SHEET_URL = "https://api.sheety.co/2caab50b1b306e932c68ca383004f671/2025FlightDeals/prices"
USERNAME = "Shane"
PW = "Shieh7732%"
AUTH = (USERNAME, PW)
# AMADEUS_API
API_KEY = "6G7wx33iVcdEtwAGPcxfPARKHjGvy4a2"
API_SECRET = "9Wln5LnAOxAFcQvS"
AMADEUS_URL_TOKEN = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_DESTINATION_URL = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
AMADEUS_IATA_SEARCH = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
# Token receive by AMADEUS
data = {
    "grant_type": "client_credentials",
    "client_id": API_KEY,
    "client_secret": API_SECRET
}

token_request = requests.post(url=AMADEUS_URL_TOKEN, data=data)
access_token = token_request.json()["access_token"]
# API call
destination_body = {
    "origin": "PAR",
    "maxPrice": "200"
}
headers = {
        "Authorization": f"Bearer {access_token}",
    }
# destination_request = requests.get(url=AMADEUS_DESTINATION_URL, headers=headers, params=destination_body)
# print(destination_request.text)
#Search iata code
iata_code_search = {
    "keyword": "Taipei"
}
# iata_response = requests.get(url=AMADEUS_IATA_SEARCH, headers=headers, params=iata_code_search)
# print(iata_response.text)
# iata_code = iata_response.json()["data"][0]["iataCode"]
# print(iata_code)

#Search data on google sheet
# google_sheety_response = requests.get(url=GOOGLE_SHEET_URL, auth=AUTH)
# print(google_sheety_response.json())
# sheet_data = google_sheety_response.json()["prices"]

# print(sheet_data)
#Loop through each row and update
# for row in sheet_data:
#     row_of_city = row["city"]
#     row_id = row["id"]
#     iata_code_search_2 = {
#         "keyword": row_of_city
#     }
#     iata_response_2 = requests.get(url=AMADEUS_IATA_SEARCH, headers=headers, params=iata_code_search_2)
#     iata_code_2 = iata_response_2.json()["data"][0]["iataCode"] # return each correct iata code
#     # print(iata_code_2)
#     update_data = {
#         "price": {
#         "iataCode": iata_code_2
#     }
#     }
#     update_url = f"{GOOGLE_SHEET_URL}/{row_id}"
#     update_iata = requests.put(url=update_url, json=update_data, auth=AUTH)
    # print(f"Updated row {row_id}: {iata_code_2}")
    # print(f"Updating row {row_id}: {iata_code_2}")
    # print("Response Status Code:", update_iata.status_code)
    # print("Response Body:", update_iata.json())  # This will show Sheety's response

#Price search
# Get today's date
today = datetime.now()
formatted_today = today.strftime("%Y-%m-%d")

# Departure: 1 month later from today
departure_date = today + relativedelta(months=1)
from_formatted_date = departure_date.strftime("%Y-%m-%d")

# Return: 5 days after departure
return_date = departure_date + relativedelta(days=5)
to_formatted_date = return_date.strftime("%Y-%m-%d")
#
# print(f"{from_formatted_date}/{to_formatted_date}")

AMADEUS_PRICE_SEARCH = "https://test.api.amadeus.com/v2/shopping/flight-offers"
price_json = {
    "originLocationCode": "TPE",
    "destinationLocationCode": "OKA",
    "departureDate": from_formatted_date,
    "returnDate": to_formatted_date,
    "adults": 1,
    "nonStop": "true",
    "currencyCode": "TWD",
    "max": "3"
}
price_response = requests.get(url=AMADEUS_PRICE_SEARCH, headers=headers, params=price_json)

first_flight = price_response.json()["data"][0]
price = float(first_flight["price"]["grandTotal"])
departure_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
return_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
return_date = first_flight["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]

# print(f"{departure_date}/{return_date}")


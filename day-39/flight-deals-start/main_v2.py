from flight_data import get_cheapest_price
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
import time

from whatsapp import WhatsappNotification
#Fix parameter
DEPARTURE_AIRPORT = "TPE"
#Find google sheet data
data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()#Receive sheet_data in json form
pprint(sheet_data)
#Looking for IATA code and update if absence
# if sheet_data[0]["iataCode"] == "":
#     flight = FlightSearch()
#     for row in sheet_data:
#         row_id = row["id"]
#         row_of_city = row["city"]
#         iata_code = flight.destination_code(row_of_city)
#         print(iata_code)
#         data_manager.update_iata_code(iata_code, row_id)

#Another way to update the whole destination_data first then update to google sheet
# if sheet_data[0]["iataCode"] == "":
#     flight = FlightSearch()
#     for row in sheet_data:
#         row_id = row["id"]
#         row_of_city = row["city"]
#         iata_code = flight.destination_code(row_of_city)
#         row["iataCode"] = iata_code
#         data_manager.destination_data = sheet_data
#         data_manager.update_destination_code()
#Define the date
today = datetime.now()
formatted_today = today.strftime("%Y-%m-%d")
months_later = today + timedelta(weeks=12)
formatted_departure_date = months_later.strftime("%Y-%m-%d")
return_date = months_later + timedelta(days=5)
formatted_return_date = return_date.strftime("%Y-%m-%d")

#Looking for IATA code and update if absence
iata_code_missing = False
flight_search = FlightSearch()

for row in sheet_data:
    if row.get("iataCode", "") == "":
        iata_code_missing = True # Start finding the iata code for the city
        row_id = row["id"]
        row_of_city = row["city"]
        iata_code = flight_search.destination_code(row_of_city)
        data_manager.update_iata_code(iata_code, row_id)
        # Update the row in sheet_data with the newly found IATA code
        row["iataCode"] = iata_code  # ✅ Update locally
        print(f"Find IATA Code: {iata_code} for {row_of_city}")


for row in sheet_data:
    row_id = row["id"]
    row_of_city = row["city"]
    row_of_iata_code = row["iataCode"]
    target_price = row["lowestPrice"]
    flights_information = flight_search.check_flight(departure_airport=DEPARTURE_AIRPORT,
                               arrival_airport=row_of_iata_code,
                               departure_date=formatted_departure_date,
                               return_date=formatted_return_date)
    cheapest_flight_information = get_cheapest_price(flights_information)
    cheapest_price = cheapest_flight_information.price
    if cheapest_flight_information is None or cheapest_price is None:
        print(f"No flight information for {row_of_city} yet!!")
        continue
    context = f"The cheapest price bound for {row_of_city} at {formatted_departure_date} and return at {formatted_return_date} is {cheapest_price}NTD"

    try:
        target_price = int(target_price)
        cheapest_price = int(cheapest_price)
    except ValueError:
        print(f"No price for this {row_of_city} at {formatted_departure_date}!")
        continue

    if int(target_price) > int(cheapest_price):
        try:
            print(context)
            send_whatsapp = WhatsappNotification()
            send_whatsapp.send_whatsapp(context)
            time.sleep(6)
        except Exception as error_message:
            print(f"Error sending Whatsapp message; {error_message}")
    else:
        print(f"Price bounding for {row_of_city} isn't the best deal")






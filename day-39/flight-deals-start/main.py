from flight_data import get_cheapest_price
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from whatsapp import WhatsappNotification
#Fix parameter
DEPARTURE_AIRPORT = "TPE"
#Find google sheet data
data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
pprint(sheet_data)


# #Looking for IATA code and update if absence
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
if sheet_data[0]["iataCode"] == "":
    flight = FlightSearch()
    for row in sheet_data:
        row_id = row["id"]
        row_of_city = row["city"]
        iata_code = flight.destination_code(row_of_city)
        print(iata_code)
        data_manager.update_iata_code(iata_code, row_id)
# Search for the flight
else:
    for row in sheet_data:
        arrival_airport = row["iataCode"]
        target_price = row["lowestPrice"]
        # print(target_price)
        flight_search = FlightSearch()
        flights_information = flight_search.check_flight(departure_airport=DEPARTURE_AIRPORT,
                                                         departure_date=formatted_departure_date,
                                                         return_date=formatted_return_date,
                                                         arrival_airport=arrival_airport)
        cheapest_flight = get_cheapest_price(flights_information)
        context = f"Departure to {row["city"]} at {formatted_departure_date}: NT${cheapest_flight.price}"
        print(context)
        if int(target_price) > int(cheapest_flight.price):
            try:
                notification = WhatsappNotification()
                notification.send_whatsapp(context)
            except cheapest_flight.price is None or cheapest_flight is None:
                print("We don't have this flight information!!")
                continue


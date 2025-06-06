from flight_search import FlightSearch
from datetime import datetime, timedelta
from data_manager import DataManager

#Define the date
today = datetime.now()
formatted_today = today.strftime("%Y-%m-%d")
months_later = today + timedelta(weeks=12)
formatted_departure_date = months_later.strftime("%Y-%m-%d")
return_date = months_later + timedelta(days=5)
formatted_return_date = return_date.strftime("%Y-%m-%d")
#Check return json data structure
# DEPARTURE = "TPE"
# ARRIVAL = "MUC"
#
# flight_data = FlightSearch()
# flights_info = flight_data.check_flight(departure_airport=DEPARTURE,
#                                          arrival_airport=ARRIVAL,
#                                          departure_date=formatted_departure_date,
#                                          return_date=formatted_return_date, is_direct=True)
# print(flights_info)

#Check google sheet userlist
# google_sheet_data = DataManager()
# user_email_list = google_sheet_data.get_user_email()
# for email in user_email_list:
#     print(email)
#     google_sheet_data.send_email()

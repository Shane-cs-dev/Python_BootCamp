
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_airport, arrival_airport, departure_date, return_date):
        self.price = price
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_date = departure_date
        self.return_date = return_date


def get_cheapest_price(data):
    if data is None or not data["data"]:
        print("No flight data")
        return FlightData("N/A", "N/A",  "N/A", "N/A", "N/A")
    #Define the data with the first flight
    first_flight = data["data"][0]
    lowest_price = round(float(first_flight["price"]["grandTotal"]))
    departure_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    return_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]
    #
    cheapest_flight = FlightData(lowest_price, departure_airport, return_airport, departure_date, return_date)
    #Loop through all the data
    for flight in data["data"]:
        price = round(float(flight["price"]["grandTotal"]))
        if price < lowest_price:
            lowest_price = price
            departure_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            return_airport = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            departure_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, departure_airport, return_airport, departure_date, return_date)
            # print(f"lowest price to {departure_airport} at {departure_date} is {lowest_price}")

    return cheapest_flight



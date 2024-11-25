from fetching_data import WeatherDataFetcher
from parsing_data import WeatherDataParser

class UserInterface:

    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = WeatherDataParser()

    def display_weather(self, city):
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse_weather_data(data)
            print(weather_report)

    def get_detailed_forecast(self, city):
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)
    
    def run(self):

        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == "exit":
                break

            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == "yes":
                forecast = self.get_detailed_forecast(city)
                print(forecast)
            else:
                self.display_weather(city)
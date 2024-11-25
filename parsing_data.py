class WeatherDataParser:

    @staticmethod
    def parse_weather_data(data):
        if not data:
            return "Weather data not available."
        
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
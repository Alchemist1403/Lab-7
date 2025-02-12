import json
import os
import requests

while True:
    try:
        city_name = input("The weather in which city do you want to know? ")
        os.system('cls')
        key = "your key" 
        data = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
        results = json.loads(data.text)

        print(f"Weather in {city_name}!\n"
        f"Main weather: {results['weather'][0]['main']}\n"
        f"Temperature: {round(results['main']['temp'] -273)}°C (feels like {round(results['main']['feels_like']-273)}°C)\n"
        # f"Max. temperature: {round(results['main']['temp_max'] -273)}°C\n"
        # f"Min. temperature: {round(results['main']['temp_min']) -273}°C\n"
        f"Air pressure: {results['main']['pressure']} hPa\n"
        f"Humidity: {results['main']['humidity']} %\n"
        f"Wind speed: {results['wind']['speed']} metre/sec\n"
        )
    except KeyError:
        print("Sorry.. We can`t find data about the weather in this city.\n")
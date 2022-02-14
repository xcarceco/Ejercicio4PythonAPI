import json
import datetime
import requests
res = requests.get('https://openweathermap.org')
print(res)

url = "https://api.openweathermap.org/data/2.5/weather&"
city_name = input("Enter city name : ")

base_url = "http://api.openweathermap.org/data/2.5/weather?"

complete_url = base_url + "appid=" +"aac7968aca75d9b2b5b6f7fcfb076e52"+ "&q=" + city_name+"&units=metric"

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    temperature_max = y["temp_max"]
    temperature_min = y["temp_min"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    print(" Temperature maximum(in celsius unit) = " +
          str(temperature_max) +
          "\n Temperature minimum(in celsius unit) = " +
          str(temperature_min) +
          "\n humidity(in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")
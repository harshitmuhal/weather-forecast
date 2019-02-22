import requests


def weather_details(city_name):
    api_key = "@@@@@@@"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    comp_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(comp_url)
    x = response.json()
    if x["cod"] != "404":
        print("Temperature (in kelvin unit) = ", x['main']['temp'], "\nMinimum Temperature (in kelvin unit) = ",
              x['main']['temp_min'],
              "\nMaximum Temperature (in kelvin unit) = ", x['main']['temp_max'],
              "\nAtmospheric pressure (in hPa unit) = ",
              x['main']['pressure'], "\nHumidity (in percentage) =",
              x['main']['humidity'], "\nVisibility (in metre unit)=", x['visibility'], "\nWind speed(in km/hr unit) =",
              x['wind']['speed'],
              "\nDescription = ", x['weather'][0]["description"])
    else:
        print('city not found')


city = input("enter city name")
weather_details(city)

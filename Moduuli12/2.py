import requests
from dotenv import dotenv_values

def get_weather(city: str): 
    api_key = dotenv_values('.env')['weather_api_key']
    request = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    try:
      response = requests.get(request)
      if response.status_code == 200:
        json_response = response.json()
        return json_response['weather'][0]['description'], json_response['main']['temp']
    except requests.exceptions.RequestException as e:
      return f"Request could not be completed, {e}"
    return ""

def kelvin_to_c(temp: int) -> str:
  kelvin = 273.15
  return "{:.2f}".format(temp-kelvin)


def main() -> None:
  get_city = input("City name: ").lower()
  weather = get_weather(get_city)
  print(f"Weather in {get_city} is {weather[0]} and the temperature is {kelvin_to_c(int(weather[1]))} degrees celsius")


if __name__=="__main__":
  main()
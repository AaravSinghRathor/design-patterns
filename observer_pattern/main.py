from observer import PhoneDisplay
from observable import WeatherStation
def main():
    weather_station = WeatherStation()
    phone_display1 = PhoneDisplay(weather_station)
    phone_display2 = PhoneDisplay(weather_station)
    weather_station.add(phone_display1)
    weather_station.add(phone_display2)
    weather_station.notify()

if __name__ == "__main__":
    main()
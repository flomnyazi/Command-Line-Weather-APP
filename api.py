import pyowm
#imports pyowm library that contains weather data from Python
print ("Welcome to our Weather Forecast Console App ")

api_key = pyowm.OWM("833fb40410275d3ccdb66126e8f04e5a")
#This creates a a variable api_key that contains the api_key to be used 
forecast = api_key.weather_at_place("Nairobi,Kenya")
#The variable forecast sets the place whose weather we wish to view
w = forecast.get_weather()
#This variable shortens the GET request function that will obtain the weather data
wind = w.get_wind
temperature = w.get_temperature('celsius')
tomorrow = pyowm.timeutils.tomorrow()
#this creates a variable tomorrow that tells the next day's weather

print (w)
print (wind)
print (temperature)
print(tomorrow)
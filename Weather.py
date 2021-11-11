import pip._vendor.requests

city = input("What city would you like to see the current weather of?:")

#API key for free api service
API="6a3fc514105cf02aa26838f5d0460c77"
URL="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API+"&units=imperial"

request = pip._vendor.requests.get(URL)
requestJson = request.json()

weatherDescription = requestJson.get("weather")[0].get("description")
weatherTemp = requestJson.get("main").get("temp")
print("Today's current forecast in "+city+", is", weatherDescription+" with a current temperature of",str(weatherTemp)+ " degrees")
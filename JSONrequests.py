import pip._vendor.requests

response = pip._vendor.requests.get("http://api.open-notify.org/astros.json")
json = response.json()
print(json)
print(json["people"])


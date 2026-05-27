from geopy.geocoders import Nominatim

geo = Nominatim(user_agent="my_app")

location = geo.geocode("Delhi")

print(location.latitude)
print(location.longitude)
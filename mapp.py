import folium
import pandas as pd
data=pd.read_csv("volcanos.csv")
lat=list(data["Latitude"])
lan=list(data["Longitude"])

map=folium.Map(location=[28.61,77.20],zoom_start=4,tiles="OpenStreetMap")
fg=folium.FeatureGroup(name="My Map")
for lt,ln in zip(lat,lan):
    fg.add_child(folium.Marker(location=[lt,ln],popup=, icon=folium.Icon(color='green')))


map.add_child(fg)    
map.save("map1.html")


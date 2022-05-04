import folium
import pandas as pd

data = pd.read_csv("in.csv")
lat = list(data["lat"])
lon = list(data["lng"])
nam = list(data["city"])

map = folium.Map(location=[28.65, 77.25], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
#add markers
for lt, ln, name in zip(lat,lon, nam):
    fg.add_child(folium.Marker(location=[lt, ln], popup=name, icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

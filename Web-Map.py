import folium
import pandas as pd

data = pd.read_csv("in.csv")
lat = list(data["lat"])
lon = list(data["lng"])
nam = list(data["city"])
cap = list(data["capital"])

def color_producer(capital):
    if capital == "admin":
        return 'red'
    else:
        return 'green'

map = folium.Map(location=[28.65, 77.25], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
#add markers
for lt, ln, name, cp in zip(lat,lon, nam, cap):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=5, popup=name, fill_color=color_producer(cp), color='grey', fill_opacity=0.7))

map.add_child(fg)

map.save("Map1.html")

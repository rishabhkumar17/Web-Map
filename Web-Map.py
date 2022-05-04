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

fgc = folium.FeatureGroup(name="City")
#add markers
for lt, ln, name, cp in zip(lat,lon, nam, cap):
    fgc.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=name, fill_color=color_producer(cp), color='grey', fill_opacity=0.7))

fgl = folium.FeatureGroup(name="Layer")
#add layer
fgl.add_child(folium.GeoJson(data=open('Indian_States.geojson', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green'}))

map.add_child(fgl)
map.add_child(fgc)
map.add_child(folium.LayerControl())

map.save("Map1.html")

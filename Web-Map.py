import folium

map = folium.Map(location=[28.65, 77.25], zoom_start=6, tiles = "Stamen Terrain")

#add market
map.add_child(folium.Marker(location=[28.65, 77.25], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.save("Map1.html")

import folium
locations = [
    (28.575050, 77.214310),
    (28.587589, 77.312897),
    (24.9965,90.3336),
    (27.42397,77.09922),
    (22.58081126380504, 88.4520462147854),
    (22.541040, 88.356430),
    (17.477100, 78.572450),
    (23.038940, 72.554950)
]
map = folium.Map(location=locations[0], zoom_start=5)

for lat, lon in locations:
    folium.Marker(location=[lat, lon]).add_to(map)

map.save("map.html")

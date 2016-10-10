import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")

#map starting point.
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=5,tiles="Stamen Terrain")

#marker color elector
def color(elev):
    minimum = int(min(df['ELEV']))
    maximum  = int(max(df['ELEV']))
    step = int((maximum-minimum)/3)

    if elev in range(minimum,step+minimum):
        col = 'green'
    elif elev in range(minimum+step,minimum+step*2):
        col = 'orange'
    else:
        col = 'red'


for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.add_child(folium.Marker(location=[lat,lon],popup=name, icon=folium.Icon(color(elev),icon_color='black')))



map.save(outfile='test3.html')

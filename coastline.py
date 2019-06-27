import geopandas as gpd
import pandas as pd
import os

data = gpd.read_file(os.path.join('data','coastline.geojson'))

x = []
y = []

for i in data.geometry:
    for value in i.coords.xy[0]:
        x.append(value)
    for value in i.coords.xy[1]:
        y.append(value)

df = pd.DataFrame({'x': x, 'y' : y})

df.to_csv(os.path.join('data','coastline.csv'))
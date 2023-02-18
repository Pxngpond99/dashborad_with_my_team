# 3rd party modules
import pandas as pd
import geopandas as gpd
import shapely
# needs 'descartes'

import matplotlib.pyplot as plt

df = pd.read_csv("data_analize/data/laclon.csv")
# initialize an axis
fig, ax = plt.subplots(figsize=(8,6))
# plot map on axis
countries = gpd.read_file(  
     gpd.datasets.get_path("naturalearth_lowres"))
countries[countries["name"] == "Thailand"].plot(color="lightgrey",
                                                 ax=ax)
# plot points
df.plot(x="lon", y="lac", kind="scatter", 
        c="brightness", colormap="YlOrRd",ax=ax)
plt.show()




















# gdf = gpd.GeoDataFrame(df.drop(['lac', 'lon'], axis=1),
#                        crs={'init': 'epsg:4326'},
#                        geometry=[shapely.geometry.Point(xy)
#                                  for xy in zip(df.lon, df.lac)])
# print(gdf)

# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# base = world.plot(color='white', edgecolor='black')
# gdf.plot(ax=base, marker='o', color='green', markersize=5)

# plt.show()
# df = pd.DataFrame({'city': ['Berlin', 'Paris', 'Munich'],
#                    'latitude': [52.518611111111, 48.856666666667, 48.137222222222],
#                    'longitude': [13.408333333333, 2.3516666666667, 11.575555555556]})
# gdf = gpd.GeoDataFrame(df.drop(['latitude', 'longitude'], axis=1),
#                        crs={'init': 'epsg:4326'},
#                        geometry=[shapely.geometry.Point(xy)
#                                  for xy in zip(df.longitude, df.latitude)])
# print(gdf)

# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# base = world.plot(color='white', edgecolor='black')
# gdf.plot(ax=base, marker='o', color='red', markersize=5)

# plt.show()
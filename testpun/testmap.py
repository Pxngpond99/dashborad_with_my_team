# 3rd party modules
import pandas as pd
import geopandas as gpd
import shapely
# needs 'descartes'

import matplotlib.pyplot as plt

df = pd.DataFrame({'city': ['Berlin', 'Paris', 'Munich'],
                   'latitude': [52.518611111111, 48.856666666667, 48.137222222222],
                   'longitude': [13.408333333333, 2.3516666666667, 11.575555555556]})
gdf = gpd.GeoDataFrame(df.drop(['latitude', 'longitude'], axis=1),
                       crs={'init': 'epsg:4326'},
                       geometry=[shapely.geometry.Point(xy)
                                 for xy in zip(df.longitude, df.latitude)])
print(gdf)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
base = world.plot(color='white', edgecolor='black')
gdf.plot(ax=base, marker='o', color='red', markersize=5)

plt.show()
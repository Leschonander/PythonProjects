from geojson import Feature, Point, FeatureCollection
from data import cordDict

points = []
for i in range(0, len(cordDict)):
    point = Feature(geometry=Point(
    (cordDict[i]['Long'],
     cordDict[i]['Lat'])))
    points.append(point)

locations = FeatureCollection(points)

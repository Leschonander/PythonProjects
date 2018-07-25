from geojson import Feature, Point, FeatureCollection
from data import cordDict

#Can't use a loop for some reason so have to do this...
#Argh
feature1 = Feature(geometry=Point(
    (cordDict[0]['Long'],
     cordDict[0]['Lat'])))
feature2 = Feature(geometry=Point(
    (cordDict[1]['Long'],
     cordDict[1]['Lat'])))
feature3 = Feature(geometry=Point(
    (cordDict[2]['Long'],
     cordDict[2]['Lat'])))
feature4 = Feature(geometry=Point(
    (cordDict[3]['Long'],
     cordDict[3]['Lat'])))
feature5 = Feature(geometry=Point(
    (cordDict[4]['Long'],
     cordDict[4]['Lat'])))
feature6 = Feature(geometry=Point(
    (cordDict[5]['Long'],
     cordDict[5]['Lat'])))
feature7 = Feature(geometry=Point(
    (cordDict[6]['Long'],
     cordDict[6]['Lat'])))
feature8 = Feature(geometry=Point(
    (cordDict[7]['Long'],
     cordDict[7]['Lat'])))
feature9 = Feature(geometry=Point(
    (cordDict[8]['Long'],
     cordDict[8]['Lat'])))
feature10 = Feature(geometry=Point(
    (cordDict[9]['Long'],
     cordDict[9]['Lat'])))
feature11 = Feature(geometry=Point(
    (cordDict[10]['Long'],
     cordDict[10]['Lat'])))

bikeLocations = (FeatureCollection([
    feature1, feature2,
    feature3, feature4,
    feature5, feature6,
    feature7, feature8,
    feature9, feature10, feature11]))
# print(bikeLocations)
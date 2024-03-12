import json
import datetime
from typing import List
from geo import calculate_distance
#this is the import statements, used in every code
start = datetime.datetime.now()
#tracking the time
def sort(top10):
    top10.sort(key = lambda x: x["distance"])
    return top10
#sorting 
top10 = []
#empty list
lat1 = 43.649637
lon1 = -79.375525
basepoint = (lat1,lon1)
#base cords
datafile='Fire Hydrants Data.json'
f = open(datafile,"rt",encoding='ascii', errors='ignore')
data_json = f.read()
f.close()
data = json.loads(data_json)
#reading the file
fire_hydrants = data['features']
#going through the data and finding what we need
for fh in fire_hydrants:
    lat = fh["geometry"]["coordinates"][1]
    lon = fh["geometry"]["coordinates"][0]
    point = (lat,lon)
    distance = calculate_distance(basepoint,point)
    fh["distance"] = distance
    top10.append(fh)
    sort(top10)
    if len(top10) > 10:
        sort(top10)
        top10.pop()
#for loop to go through the fire hydrants and sort them
print(top10)
#printing them, it didn't format in a way I wanted so I just kept it as is.
end = datetime.datetime.now()
duration = end - start
print(f"This took {duration} to calculate")
#tracking and printing the amount of time.

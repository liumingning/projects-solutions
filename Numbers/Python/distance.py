# Distance Between Two Cities
# Calculates the distance between two cities and allows the user to specify a unit of distance.
# This program may require finding coordinates for the cities like latitude and longitude.

from pygeocoder import Geocoder
from math import radians, cos, sin, asin, sqrt
import sys

EARTH_RADIUS = 6378

def haversine(lat1, lon1, lat2, lon2):

  lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

  dlon = lon2 - lon1
  dlat = lat2 - lat1
  a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
  c = 2 * asin(sqrt(a))

  km = EARTH_RADIUS * c
  return km

f = raw_input("From: ")
t = raw_input("To: ")
measure = raw_input("Meters or Kilometers? [km/m] ")
if measure == "m":
  result = 1000
elif measure == "km":
  result = 1
else:
  sys.exit("Invalid option")

print "Calculating..."
fr = Geocoder.geocode(f)
tr = Geocoder.geocode(t)

print "Distance from [" + str(fr[0]) + "] to [" + str(tr[0]) + "]"
final_result = result * haversine(fr.coordinates[0], fr.coordinates[1], tr.coordinates[0], tr.coordinates[1])

print str(final_result) + measure


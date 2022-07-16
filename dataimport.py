# Bruce Bjostad Student ID:009839410
import csv

from hash import HashMap
from package import Package
from distance import distance


#Create 2d array of distances from csv
#Create dict of addresses from csv
#return distance object
#O(N^3)
def create_atlas():
    distances = []
    with open("./data/distances.csv", "r", encoding='utf-8-sig') as distance_csv:
        for row in csv.reader(distance_csv, delimiter=','):
            distances.append([float(d) for d in row])
    locations = {}
    with open("./data/locations.csv", "r", encoding='utf-8-sig') as location_csv:
        for row in csv.reader(location_csv, delimiter=','):
            locations[row[2].strip()] = row
    return distance(distances, locations)


#import packages and sort them via the created hash class
#O(N)
def collect_packages():
    sorted_packages = HashMap()
    with open("./data/packages.csv", "r", encoding='utf-8-sig' ) as package_csv:
        for p in csv.reader(package_csv, delimiter=','):
            new_package = Package(int(p[0]), p[1], p[2], p[3], int(p[4]), p[5], "AT WGUPS HUB")
            sorted_packages.add_package(new_package)
    return sorted_packages


hashed_packages = collect_packages()
atlas = create_atlas()



print(atlas.get_index("1330 2100 S"))
print(atlas.get_index("2010 W 500 S"))
print(("1330 2100 S", "1330 2100 S"))
print(atlas.get_distance("1330 2100 S", "5100 South 2700 West"))

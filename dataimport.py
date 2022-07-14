# Bruce Bjostad Student ID:009839410
import csv

from hash import HashMap
from package import Package
from distance import distance


def distance_map():
    distances = []
    with open("./data/distances.csv", "r", encoding='utf-8-sig') as distance_csv:
        for row in csv.reader(distance_csv, delimiter=','):
            distances.append([float(d) for d in row])
    return distances

def location_index():
    locations = []
    with open("./data/locations.csv", "r", encoding='utf-8-sig') as location_csv:
        for loc in csv.reader(location_csv, delimiter=','):
            locations.append(loc)
    return locations


#import packages and sort them via the created hash class
#O(N)
def collect_packages():
    sorted_packages = HashMap()
    with open("./data/packages.csv", "r", encoding='utf-8-sig' ) as package_csv:
        manifest = csv.reader(package_csv, delimiter=',')
        for p in manifest:
            new_package = Package(int(p[0]), p[1], p[2], p[3], int(p[4]), p[5], "AT WGUPS HUB")
            sorted_packages.add_package(new_package)
    return sorted_packages


hashed_packages = collect_packages()
test = distance()
print(test.get_distance("6351 South 900 East", "600 E 900 South"))

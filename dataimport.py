# Bruce Bjostad Student ID:009839410
import csv

from hash import HashTable
from package import Package
from distance import Distance


# Create 2d array of distances from csv
# Create dict of addresses from csv
# return distance object
# O(N^2) Time complexity
# O(N) Space complexity
def create_atlas():
    distances = []
    with open("./data/distances.csv", "r", encoding='utf-8-sig') as distance_csv:
        for row in csv.reader(distance_csv, delimiter=','):
            distances.append([float(d) for d in row])
    locations = {}
    with open("./data/locations.csv", "r", encoding='utf-8-sig') as location_csv:
        for row in csv.reader(location_csv, delimiter=','):
            locations[row[2].strip()] = row
    return Distance(distances, locations)


# Import packages and sort them via the created hash class
# O(N)
def collect_packages():
    sorted_packages = HashTable()
    with open("./data/packages.csv", "r", encoding='utf-8-sig' ) as package_csv:
        for p in csv.reader(package_csv, delimiter=','):
            new_package = Package(int(p[0]), p[1], p[2], p[3], int(p[4]), p[5], "AT WGUPS HUB")
            sorted_packages.add_package(new_package)
    return sorted_packages


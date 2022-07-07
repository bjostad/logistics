# Bruce Bjostad Student ID:009839410
import csv
from hash import HashTable


def collect_packages():
    sorted_packages = HashTable()
    with open("./data/packages.csv", "r", encoding='utf-8-sig' ) as package_csv:
        manifest = csv.reader(package_csv, delimiter=',')
        for p in manifest:
            sorted_packages.add_package(p)
    return sorted_packages


hashed_packages = collect_packages()
print(hashed_packages)

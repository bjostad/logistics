# Bruce Bjostad Student ID:009839410

class HashMap:

    # Construct a list of 10 empty lists
    # O(N)
    def __init__(self):
        self.map = []
        for i in range(10):
            self.map.append([])

    # Find the proper list for the package to be added to by using package ID % list length
    # Add package to the nested list inside the list
    # O(1)
    def add_package(self, package):
        key = package.id
        bucket = key % len(self.map)
        self.map[bucket].append(package)

    # Find package by id
    # Remove package if found in nested list
    # O(N)
    def remove_package_by_id(self, package_id):
        bucket = int(package_id) % len(self.map)
        for p in self.map[bucket]:
            if p[0] == int(package_id):
                self.map[bucket].remove(p)

    # Find package by package object
    # Remove package if found in nested list
    # O(N)
    def remove_package_by_package(self, package):
        bucket = int(package[0]) % len(self.map)
        if package in self.map[bucket]:
            self.map[bucket].remove(package)

    # Find the proper list for the package and iterate through the nested list to determine if it exists
    # If found, return found package
    # O(N)
    def find_package(self, package_id):
        bucket = int(package_id) % len(self.map)
        for p in self.map[bucket]:
            if p.id == int(package_id):
                return p

    #Return number of package objects in hashed package map
    #O(N^2)
    def __len__(self):
        i = 0
        for bucket in self.map:
            for _p in bucket:
                i = i + 1
        return i

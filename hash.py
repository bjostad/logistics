# Bruce Bjostad Student ID:009839410

# SELF ADJUSTING DATA STRUCTURE
# This class creates a hash table that stores package data in lists nested in a list
# The number of lists containing packages, referred to as buckets, is determined by the buckets instance variable
# Each bucket can contain a list of 0 to N packages
# The correct bucket for each package is determined by the package id % buckets variable
# Package is then store in the list representing that bucket
class HashTable:

    # Construct a list of 10 empty lists
    # O(N)
    def __init__(self):
        # buckets instance variable determines the number of buckets for the hash table
        self.buckets = 10
        self.map = []
        for i in range(self.buckets):
            self.map.append([])

    # Find the proper list for the package to be added to by using package ID % buckets
    # Add package to the nested list inside the list
    # O(1)
    def add_package(self, package):
        key = package.id
        bucket = key % self.buckets
        self.map[bucket].append(package)

    # Find the proper bucketlist for the package
    # Iterate through the nested list to determine if it exists
    # Remove package if found in nested list
    # O(N)
    def remove_package_by_id(self, package_id):
        bucket = int(package_id) % self.buckets
        for p in self.map[bucket]:
            if p.id == int(package_id):
                self.map[bucket].remove(p)

    # Find the proper bucketlist for the package
    # Iterate through the nested list to determine if it exists
    # Remove package if found in nested list
    # O(N)
    def remove_package_by_package(self, package):
        bucket = int(package.id) % self.buckets
        if package in self.map[bucket]:
            self.map[bucket].remove(package)

    # Find the proper bucketlist for the package
    # Iterate through the nested list to determine if it exists
    # If found, return found package
    # O(N)
    def find_package(self, package_id):
        bucket = int(package_id) % self.buckets
        for p in self.map[bucket]:
            if p.id == int(package_id):
                return p

    # Return number of package objects in hashed package map
    # O(N^2)
    def __len__(self):
        i = 0
        for bucket in self.map:
            for _p in bucket:
                i = i + 1
        return i

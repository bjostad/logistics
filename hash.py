# Bruce Bjostad Student ID:009839410

class HashTable:

    #Construct a list of 10 empty lists
    #O(N)
    def __init__(self):
        self.table = []
        for i in range(10):
            self.table.append([])

    #Find the proper list for the package to be added to by using package ID % list length
    #Add package to the nested list inside the list
    #O(1)
    def add_package(self, package):
        key = int(package[0])
        bucket = key % len(self.table)
        self.table[bucket].append(package)

    #Find the proper list for the package and iterate through the nested list to determine if it exists
    #Remove package if found in nested list
    #O(N)
    def remove_package(self, package):
        key = int(package[0])
        bucket = key % len(self.table)
        if key in self.table[bucket]:
            self.table[bucket].remove(package)

    #Find the proper list for the package and iterate through the nested list to determine if it exists
    #If found, return found package
    #O(N)
    def find_package(self, package):
        key = int(package[0])
        bucket = key % len(self.table)
        for p in self.table[bucket]:
            if p[0] == key:
                return p



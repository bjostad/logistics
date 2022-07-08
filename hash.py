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
        key = int(package[0])
        bucket = key % len(self.map)
        self.map[bucket].append(package)

    # Find the proper list for the package and iterate through the nested list to determine if it exists
    # Remove package if found in nested list
    # O(N)
    def remove_package_by_id(self, package_id):
        bucket = int(package_id) % len(self.map)
        for p in self.map[bucket]:
            if p[0] == package_id:
                self.map[bucket].remove(p)

    # Find the proper list for the package and iterate through the nested list to determine if it exists
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
            if p[0] == package_id:
                return p


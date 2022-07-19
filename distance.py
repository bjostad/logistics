# Bruce Bjostad Student ID:009839410

class Distance:

    #Constuct distance object
    def __init__(self, distance_map, location_index):
        self.distance_map = distance_map
        self.location_index = location_index

    # Lookup the index of the provided location
    # Return index
    # O(1)
    def get_index(self, address):
        return self.location_index[address][0]

    # Lookup the distance from current package to destination package
    # O(1)
    def get_distance(self, current, destination):
        current_index = int(self.get_index(current))
        destination_index = int(self.get_index(destination))
        if (current_index < destination_index):
            return float(self.distance_map[destination_index][current_index])
        else:
            return float(self.distance_map[current_index][destination_index])


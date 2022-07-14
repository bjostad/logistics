# Bruce Bjostad Student ID:009839410
import dataimport


class distance:

    def __init__(self):
        self.distance_map = dataimport.distance_map()
        self.location_index = dataimport.location_index()

    def get_index(self, address):
        for location in self.location_index:
            if location[2].strip() == address.strip(): #String compare works, but dist still is 0.0
                return location[0]

    def get_distance(self, current, destination):
        current_index = int(self.get_index(current))
        destination_index = int(self.get_index(destination))





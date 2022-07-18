# Bruce Bjostad Student ID:009839410

from datetime import timedelta

class Truck:

    def __init__(self, truck_number,start_time, stop_time, atlas):
        self.truck_number = truck_number
        self.manifest = {}
        self.distance_manifest = {}
        self.start_time = start_time
        self.stop_time = stop_time
        self.total_distance = 0.0
        self.total_delivery_time = timedelta(hours=0, minutes=0)
        self.current_location = "4001 South 700 East"
        self.atlas = atlas

    # Load package onto truck manifest
    # Set package to En Route status
    # O(1)
    def load_package(self, package):
        self.manifest[package.id] = package
        package.en_route(self.truck_number)

    # Delivery provided package
    # Add distance to truck total distance
    # Add travel time to truck total delivery time
    # Remove package from truck manifest
    # O(1)
    def deliver_package(self, package, distance):
        self.total_distance = self.total_distance + distance
        self.total_delivery_time = self.total_delivery_time + timedelta(minutes=distance/0.3)
        package.deliver(self.start_time + self.total_delivery_time)
        self.current_location = package.address
        return self.manifest.pop(package.id)

    # Begin delivering packages on truck manifest
    # Obtain next package and determine if it can be delivered in time
    # O(N^2)
    def run_route(self):
        for i in range(len(self.manifest)):
            current_package = self.next_package()
            if ((self.start_time + self.total_delivery_time +timedelta(minutes=current_package[1]/0.3)) < self.stop_time):
                self.deliver_package(current_package[0], current_package[1])
            else:
                break


    def next_package(self):
        next_package = "none"
        next_distance = 100.0
        for p in self.manifest.values():
            p_distance = self.atlas.get_distance(self.current_location, p.address)
            if p_distance < next_distance:
                next_package = p
                next_distance = p_distance
        return [next_package, next_distance]

    def return_to_hub(self):
        distance = self.atlas.get_distance(self.current_location, "4001 South 700 East")
        self.total_distance = self.total_distance + distance
        self.total_delivery_time = self.total_delivery_time + timedelta(minutes=distance / 0.3)
        self.current_location = "4001 South 700 East"


    def truck_report(self):
        print("-=-=-=-=-=-=-=- Truck " + str(self.truck_number) +" -=-=-=-=-=-=-=-")
        print("Total Time: " + str(self.total_delivery_time))
        print("Total Distance traveled: " + str(self.total_distance) + " miles")

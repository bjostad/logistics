# Bruce Bjostad Student ID:009839410

class Package:

    # Construct Package object
    def __init__(self, id: int, address: str, city: str, st: str, zip: int, deadline: str, status: str):
        self.id = id
        self.address = address
        self.city = city
        self.st = st
        self.zip = zip
        self.deadline = deadline
        self.status = status


    # Change package status to delivered and set time of delivery
    # O(1)
    def deliver(self, delivery_time):
        self.status = "Delivered at " + str(delivery_time)

    # Change package status to Loaded on Truck to show its on a truck to be delivered
    # O(1)
    def loaded(self, truck_number):
        self.status = "Loaded on Truck " + str(truck_number)


    # Change package status to En Route to show its out for delivery
    # O(1)
    def en_route(self, truck_number):
        self.status = "En Route on Truck " + str(truck_number)

    #Update Address of package
    #O(1)
    def update_address(self, address):
        self.address = address

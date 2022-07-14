# Bruce Bjostad Student ID:009839410

class Package:

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
    def deliver_package(self, delivery_time):
        self.status = "Delivered at " + delivery_time

    def en_route(self, truck_number):
        self.status = "En Route on Truck " + str(truck_number)
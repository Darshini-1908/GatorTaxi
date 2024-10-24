class Ride:
    def __init__(self, rNumb, rCost, duration_of_trip):
        self.rNumb = rNumb
        self.rCost = rCost
        self.duration_of_trip = duration_of_trip

    def less_than(self, other_ride): #less_than method is used to compare rides and determine their ordering in the min heap.
        if self.rCost < other_ride.rCost:
            return True
        elif self.rCost > other_ride.rCost:
            return False
        elif self.rCost == other_ride.rCost:
            if self.duration_of_trip > other_ride.duration_of_trip:
                return False
            else:
                return True

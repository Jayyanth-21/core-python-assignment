class Taxi:
    def __init__(self):
        self.base_fare = 50
        self.distance_fare = 10

    def calcFare(self, trips):
        total_fare = 0
        for i, distance in enumerate(trips, 1):
            fare = self.base_fare + (distance * self.distance_fare)
            total_fare += fare
            print(f"Trip {i}: ${fare}")

        print(f"Total Fare: ${total_fare}")

    def inpTrips(self):
        try:
            num_trips = int(input("Enter the number of trips: "))
            trips = []
            for i in range(num_trips):
                distance = float(input(f"Enter the distance for trip {i+1} (in km): "))
                trips.append(distance)
            self.calcFare(trips)
        except ValueError:
            print("Invalid input. Please enter valid numbers for trips and distances")

tf = Taxi()
tf.inpTrips()

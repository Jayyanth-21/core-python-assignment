class MovieTicketBooking:
    def __init__(self):
        self.total_seats = 10
        self.booked_seats = [2, 5, 7]

    def bookSeat(self, seat_number):
        if seat_number in self.booked_seats:
            print(f"Seat {seat_number} is already booked")
        elif seat_number > self.total_seats or seat_number < 1:
            print(f"Invalid seat number. Please select a seat between 1 and {self.total_seats}")
        else:
            self.booked_seats.append(seat_number)
            print(f"Seat {seat_number} booked successfully.")

    def cancelSeat(self, seat_number):
        if seat_number not in self.booked_seats:
            print(f"Seat {seat_number} is not booked yet")
        else:
            self.booked_seats.remove(seat_number)
            print(f"Seat {seat_number} booking has been cancelled")

    def displaySeats(self):
        print(f"\nTotal seats: {self.total_seats}")
        print(f"Booked seats: {self.booked_seats}")
        available_seats = [seat for seat in range(1, self.total_seats + 1) if seat not in self.booked_seats]
        print(f"Available seats: {available_seats}")

    def manageBooking(self):
        while True:
            self.displaySeats()
            print("1. Book a seat")
            print("2. Cancel a seat")
            print("3. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    book_seat = int(input("Enter seat number to book: "))
                    self.bookSeat(book_seat)
                elif choice == 2:
                    cancel_seat = int(input("Enter seat number to cancel: "))
                    self.cancelSeat(cancel_seat)
                elif choice == 3:
                    print("Exiting the booking system.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option (1, 2, or 3).")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

tic = MovieTicketBooking()
tic.manageBooking()

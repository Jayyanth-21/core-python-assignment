class Menu:
    def __init__(self):
        self.initial_menu = ['pizza', 'burger', 'momos', 'pasta', 'salad', 'rotis']

    def addItem(self):
        item = input("Enter the menu item you wish to add to the menu: ")
        if item not in self.initial_menu:
            self.initial_menu.append(item)
            print("Item added to the menu successfully.")
        else:
            print(f"{item} is already in the menu.")

    def remItem(self, item):
        if item in self.initial_menu:
            self.initial_menu.remove(item)
            print(f"{item} has been removed from the menu.")
        else:
            print(f"{item} is not available in the current menu.")

    def checkItem(self, item):
        if item in self.initial_menu:
            print(f"Availability: {item} is available.")
        else:
            print(f"Availability: {item} is NOT available.")

    def manipulate(self):
        print(f"Current menu: {self.initial_menu}")
        while True:
            print("Choose your choice from below:")
            print("1. Add an item        2. Remove an item")
            print("3. Check an item      4. View the final menu")
            print("5. Exit")

            try:
                ch = int(input("Enter your option: "))
                if ch == 1:
                    self.addItem()
                elif ch == 2:
                    item = input("Enter the name of the item to remove from the menu: ")
                    self.remItem(item)
                elif ch == 3:
                    item = input("Enter the name of the item to check its availability: ")
                    self.checkItem(item)
                elif ch == 4:
                    print("Final menu after updates:", self.initial_menu)
                elif ch == 5:
                    print("Exiting the menu manipulation system. Goodbye!")
                    break
                else:
                    print("Enter a valid choice (1, 2, 3, 4, or 5).")
            except ValueError:
                print("Invalid input. Please enter a number.")

ob = Menu()
ob.manipulate()

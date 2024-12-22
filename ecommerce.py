class Ecommerce:
    def __init__(self):
        self.cart = {}
    def addItem(self):
        name = input('Enter the name of the product: ')
        try:
            price = int(input("Enter the price ($): "))
            self.cart[name] = price
            print("Item added to cart successfully...")
        except ValueError:
            print("Please enter a valid price!")
        return name, price

    def delItem(self, name):
        if name in self.cart:
            self.cart.pop(name)
            print(f"{name} has been removed from the cart successfully.")
        else:
            print("Product is not available in the cart. Check the name again.")

    def calcTot(self):
        total = sum(self.cart.values())

        if len(self.cart) > 5:
            print("You are eligible for a 10% discount!")
            print(f"Your total bill before discount is :${total}")
            total *= 0.9

        print(f"Final bill is: ${total:.2f}")

    def shop(self):
        while True:
            print("\nChoose your option:")
            print("1. Add an item")
            print("2. Delete an item")
            print("3. Exit and view bill")

            try:
                ch = int(input("Enter your option: "))
                if ch == 1:
                    self.addItem()
                elif ch == 2:
                    name = input("Enter the product name to delete: ")
                    self.delItem(name)
                elif ch == 3:
                    print("Entering the billing counter...")
                    self.calcTot()
                    print("Thank you for shopping with us! Please visit again.")
                    break
                else:
                    print("Please enter a valid choice (1, 2, or 3).")
            except ValueError:
                print("Invalid input. Please enter a number.")

sh = Ecommerce()
sh.shop()

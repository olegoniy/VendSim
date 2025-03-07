from products import Product
class VM:
    """
    Vending machine class. Has an attribute self.change to keep track of the remaining change and 
    self.products to store the iformation about products in sale.
    """
    def __init__(self, change, products): #products is a list of dicts
        """Vending machine constructor."""
        self.change = change
        self.products = [Product(p["name"], p["price"], p["stock"]) for p in products] # self.products is a list of Product instances

    def __str__(self):
        """String representation of the class."""
        string = "Vending machine products\n------------------------\n"
        for i in range (len(self.products)):
            string += f"[{i+1}] {self.products[i].__str__()}\n"
        return string

    def sell_product(self, choice, money):
        """Function for selling the product and updating the amount of available change."""
        price = self.products[choice - 1].price
        if price > money:
            raise ValueError("Too little money. Please insert more")
        elif price < money and self.change < (money-price):
            raise ValueError("We have too little change. Please try inserting less money.")
        else:
            self.products[choice - 1].stock -= 1
            self.change -= (money - price)
            self.change += money
            print(f"Here you go! One {self.products[choice - 1].name}.")
            if (money - price) > 0:
                print(f"Your change: {money - price}\n")


            


        






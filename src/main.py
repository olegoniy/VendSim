import json
from vending_machine import VM
from products import Product

def load(filename="products.json"): 
    """
    Loads the amount of change available and information about products from a given file.
    Default file: products.json
    """
    with open(filename, "r") as f:
        D = json.load(f)

    change = D["change"] # an integer
    products = D["products"] # a list of dictionaries

    return change, products


def save(automat, filename="products.json"): #automat is instance of VM
    """
    Transforms a VM instance (automat) into a list of dictionaries and dumps
    it into the given file.
    Default file: products.json
    """
    product_list = []
    for p in automat.products:
        product_list.append({"name": p.name, "price": p.price, "stock": p.stock})

    D = {"change": automat.change, "products": product_list}

    with open(filename, "w") as f:
        json.dump(D, f)

def main():
    """Main function. Handles loadig from a file, deals with user input and saves the data in the end."""
    load_from_file = False
    if load_from_file:
        change, products = load()
    else:
        change = 5.0
        products = [
                {"name": "Premium Cola", "price": 1.5, "stock": 10},
                {"name": "Makava", "price": 1.4, "stock": 3},
                {"name": "Wostok", "price": 0.8, "stock": 5},
                {"name": "Club Mate", "price": 1.0, "stock": 1}
                ]

    automat = VM(change, products)

    while True:
        try:
            while True:
                try:
                    print(automat)
                    while True:
                        try:    
                            money = float(input("Please insert money:\n> "))
                            if money < 0:
                                raise ValueError
                            else:
                                break
                        except ValueError:
                            print("Please enter a valid amount of money.")
                            raise AttributeError
            
                    while True:
                        try:
                            choice = int(input("Please choose a product:\n> "))
                            if choice < 1 or choice > len(automat.products):
                                raise IndexError(f"The product with the id {choice} does not exist")
                            elif  not automat.products[choice - 1].is_in_stock:
                                raise IndexError(f"The product you've chosen is out of stock.")
                            else:
                                break
                        except (ValueError, IndexError) as e:
                            print(e)
                            raise AttributeError
        
    
                    try:
                        automat.sell_product(choice, money)
                        break
                    except ValueError as e:
                        print(e)

                except AttributeError:   
                    continue 
        
        except KeyboardInterrupt:
            save(automat)
            print(" Bye!")
            break

if __name__ == "__main__":
    main()

















    


    



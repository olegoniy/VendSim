class Product:
    """
    Class to describe each product.
    """
    def __init__(self, name, price, stock):
        """Product class constructor."""
        self.name = name 
        self.price = price
        self.stock = stock

    def __str__(self):
        """String representation to use later in string representation of VM."""
        string = f"{self.name}: {self.price} Euro "
        if self.is_in_stock:
            string += f"({self.stock} available)"
        else:
            string += f"(Out of stock)"
        return string

    def is_in_stock(self):
        """Is the product in stock?"""
        return self.stock > 0

    # decorators (setters and getters) for class attributes:
    @property
    def name(self): 
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            raise ValueError("Name should not be empty")
        else:
            self.__name = new_name

    @property
    def price(self): 
        return self.__price

    @price.setter
    def price(self, new_price):
        if not(isinstance(new_price, float)):
            raise ValueError("Price should be a float")
        elif new_price < 0:
            raise ValueError("Price should be >= 0")
        else:
            self.__price = new_price 

    @property
    def stock(self): 
        return self.__stock

    @stock.setter
    def stock(self, new_stock):
        if not(isinstance(new_stock, int)):
            raise ValueError("Stock should be an integer")
        elif new_stock < 0:
            raise ValueError("Stock should be >= 0")
        else:
            self.__stock = new_stock

    



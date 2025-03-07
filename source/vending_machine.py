from groceries import Grocerie as gr
import json
from prettytable import PrettyTable as pt


class VendingMachine():

    def __init__(self, file:str="vendStock.json"):
        self._file = file
        self._stock = []
        self._change = 0

    def _load(self):
        with open(self._file, 'r') as file:
            res = json.loads(file.read())
        self._change = res["change"]
        for product in res["groceries"]:
            grocerie = gr(product["name"], product["price"])
            self._stock.append([res["groceries"].index(product)+1, grocerie, product["stock"]])


    def _save(self):
        res = {}
        res["change"] = self._change
        res["groceries"] = []
        for product in self._stock:
            prod = {}
            prod["name"] = product[1].getName()
            prod["price"] = product[1].getCost()
            prod["stock"] = product[2]
            res["groceries"].append(prod)
        with open(self._file, 'w') as f:
            f.write(json.dumps(res))
            
    def __str__(self):
        res = pt()
        res.field_names = ["Index", "Prduct", "Price", "Left in Stock"]
        for product in self._stock:
            res.add_row([product[0], product[1].getName(), product[1].getCost(), product[2]])
        return res.get_string(sortby="Index")
    
    def buy(self, payed:float, choice:int):
        if len(self._stock) < choice:
            print(f"There is no product with index {choice}!")
            return False
        product = self._stock[choice-1]
        if product["stock"] == 0:
            print(f"Sorry, we are out of {product["name"]} right now :(")
            return False
        if payed < product["cost"]:
            print(f"The cost of {product["name"]} euros is higher, than you provided ({payed} euro)")
            return False
        if (payed - product["cost"]) > self._change:
            print(f"Sorry, I do not posess right amount of money to give you change for {self._change} euro")
            return False
        product["stock"] -= 1
        print(f"Here you go, buddy! One {product["name"]}")
        if payed != product["cost"]:
            print(f"and your change is {(payed - product["cost"])} euros")
            self._change -= payed - product["cost"]
        self._save()
        return True
        
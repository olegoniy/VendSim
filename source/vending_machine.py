from groceries import Grocerie as gr
import json
from prettytable import PrettyTable


class VendingMachine():

    def __init__(self, file:str="vendStock.json"):
        self._file = file
        self._stock = []
        self._change = 0

    def _load(self):
        try:
            with open(self._file, 'r') as file:
                res = json.loads(file.read())
            self._change = res["change"]
            for product in res["groceries"]:
                grocerie = gr(product["name"], product["price"])
                self._stock.append([res["groceries"].index(product)+1, grocerie, product["stock"]])
        except:
            print("Unfotunately, file of yours wasn't found!")

class Grocerie():

    def __init__(self, name:str, cost:float):
        self._name = name
        self._cost = cost

    def getName(self)->str:
        return self._name
    
    def getCost(self)->float:
        return self._cost
    
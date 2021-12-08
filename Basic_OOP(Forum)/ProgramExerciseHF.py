class Food:
    def __init__(self, food, pounds=0): # initialize
        self.__food = food
        self.__pounds = pounds
        self.__cost = self.getCostHF()
        self.__calc = self.calcCostHF()

    def setFoodHF(self):
        self.__food = food

    def setPoundsHF(self):
        self.__pounds = pounds

    def getFoodHF(self):
        return self.__food

    def getPoundsHF(self):
        return self.__pounds

    def __PriceList(self): # Price list
        if self.__food == "Dry Cured Iberian Ham":
            self.__cost = 177.80
        elif self.__food == "Wagyu Steaks":
            self.__cost = 450.00
        elif self.__food == "Matsutake Mushrooms":
            self.__cost = 272.00
        elif self.__food == "Kopi Luwak Coffee":
            self.__cost = 306.50
        elif self.__food == "Moose Cheese":
            self.__cost = 487.20
        elif self.__food == "White Truffles":
            self.__cost = 3600.00
        elif self.__food == "Blue Fin Tuna":
            self.__cost = 3603.00
        elif self.__food == "Le Bonnotte Potatoes":
            self.__cost = 270.81

    def getCostHF(self):
        self.__PriceList()
        return self.__cost

    def calcCostHF(self): # Calculate total
        self.__calc = self.__pounds * self.__cost
        return self.__calc
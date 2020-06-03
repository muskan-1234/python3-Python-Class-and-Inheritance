
#Q1

class Bike:

    def __init__(self, initX, initY):

        self.color = initX
        self.price = initY

testOne = Bike('blue',89.99)   
testTwo = Bike('purple',25.0)

#Q2


class AppleBasket:
    def __init__(self, apple_color, apple_quantity):

        self.apple_color = apple_color
        self.apple_quantity = apple_quantity
        
    def increase(self):
        self.apple_quantity = self.apple_quantity + 1
        
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)    

testOne = AppleBasket('red',4)
print(testOne)
testOne.increase()
print(testOne)

#Q3


class BankAccount:
    def __init__(self,name, amt):

        self.name = name
        self.amt = amt
    
    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt) 

t1 = BankAccount("Bob",100)   
print(t1)


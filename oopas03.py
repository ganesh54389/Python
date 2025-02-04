#=========================encapsulation=========================================
# checking for public access
class public():
    def __init__(self):
        self.name="john"
    def display_name(self):
        print(self.name)
object=public()
object.display_name()  
print(object.name)      
#checking for protect access
class grandfather():
    def __init__(self,a):
        self._a=a   #protected attribute
        print(f"grand father property is {a}")
class father(grandfather):
    def display(self):
        print(self._a)

object=father("100cr")
object.display()
# #checking private access
class gfather():
    def __init__(self,a):
        self.__a=a
        print(f"grand father {a}")
class father(gfather):
    def display(self):
        print(self.__a)
class child(father):
     def display01(self):# we cant have access by using private (__) to properties
        print(self.__a)
object=child("100cr")
object.display()
object.display01  
#=======================abstarction===================================
from abc import ABC,abstractmethod
class demo(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def display01(self):
        pass
class demo01(demo):
      def display(self):
        print("implemented method 01")
      def display01(self):
           print("implumentation method 02") 
object=demo01()
object.display()
object.display01()
#another example

from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
      
    @abstractmethod
    def printDetails(self):
        pass

    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Available")

car1 = Hatchback("Maruti", "Alto", "2022")
car1.printDetails()
car1.accelerate()
car1.sunroof()

    




    

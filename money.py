#File Name:   money.py
# Purpose: Holds all the methods for the class Money
# Justin Garvida 04/23/23

class Money:
    def __init__(self,dollars = 0,cents = 0):
        self.__dollars = dollars
        self.__cents = cents

    #getters
        
    def getDollars(self):
        return self.__dollars
    
    def getCents(self):
        return self.__cents
    
    #setters
    
    def setDollars(self,dollars):
        self.__dollars = dollars
    
    def setCents(self,cents):
        self.__cents = cents
    
    def addDollars(self,dollars):
        self.__dollars += dollars
        return self.__dollars
    
    def addCents(self,cents):
        self.__cents += cents
        while self.__cents >= 100:
            self.__dollars += 1
            self.__cents -= 100
        return self.__cents
    
    #Ovveride Methods
    
    def __add__(self,other):
        newDollars = self.__dollars + other.getDollars()
        newCents = self.__cents + other.getCents()
        if newCents >= 100:
            newDollars += 1
            newCents -= 100
        return Money(newDollars,newCents)
    
    def __sub__(self,other):
        if self.__dollars > other.getDollars():
            newDollars = self.__dollars - other.getDollars()
            newCents = self.__cents - other.getCents()
        else:
            newDollars = other.getDollars() - self.__dollars
            newCents = other.getCents() - self.__cents
        if newCents < 0:
            newDollars -= 1
            newCents += 100
        return Money(newDollars,newCents)
    
    def __mul__(self,integer):
        newDollars = self.__dollars * integer
        newCents = self.__cents * integer
        while newCents >= 100:
            newDollars += 1
            newCents -= 100
        return Money(newDollars,newCents)
    
    def __str__(self):
        return f"${self.__dollars}.{self.__cents:02d}"
    
    #Comparison Methods
    
    def __eq__(self,other):
        return self.__dollars == other.getDollars() and self.__cents == other.getCents()
    
    def __ne__(self,other):
        return self.__dollars != other.getDollars() and self.__cents != other.getCents()
    
    def __lt__(self,other):
        return self.__dollars < other.getDollars() and self.__cents < other.getCents()
    
    def __le__(self,other):
        return self.__dollars <= other.getDollars() and self.__cents <= other.getCents()
    
    def __gt__(self,other):
        if self.__dollars > other.getDollars():
            return True
        elif self.__dollars == other.getDollars() and self.__cents > other.getCents():
            return True
        else:
            return False
    
    def __ge__(self,other):
        if self.__dollars >= other.getDollars():
            return True
        elif self.__dollars >= other.getDollars() and self.__cents >= other.getCents():
            return True
        elif self.__dollars == other.getDollars() and self.__cents < other.getCents():
            return False
        else:
            return False
    
    def __getitem__(self,index):
        if index == 0:
            return int(self.__dollars)
        elif index == 1:
            return int(self.__cents)
        else:
            raise ExceptionError
        
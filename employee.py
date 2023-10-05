"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name,salary=0,hours = (0,0),commission = (0,0),bonus =0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.commission = commission
        self.bonus = bonus
        self.outputString = [] 

    def getSalary(self):
        self.outputString.append(" works on a monthly salary of " + str(self.salary))
        return self.salary

    def getBonus(self):
        self.outputString.append("and receives a bonus commission of " + str(self.bonus) + ".")
        return self.bonus

    def calcuateHourly(self):
        total = self.hours[0] * self.hours[1]
        self.outputString.append(" works on a contract of " + str(self.hours[0]) + " hours at " + str(self.hours[1]) + "/hour")
        return total
    
    def calculateCommission(self):
        total = self.commission[0] * self.commission[1]
        self.outputString.append("and receives a commission for " + str(self.commission[0]) + " contract(s) at " + str(self.commission[1]) + "/contract.")
        return total

    def get_pay(self):
        pay = 0
        if (self.salary > 0):
            pay += self.getSalary()
        if (self.hours[0] > 0):
            pay += self.calcuateHourly()
        if (self.commission[0] > 0):
            pay += self.calculateCommission()
        if (self.bonus > 0):
            pay += self.getBonus()
        self.outputString.append("Their total pay is " + str(pay) + ".")
        return pay

    def __str__(self):
        self.outputString.clear()
        self.get_pay()
        output = self.name
        if (self.outputString.__len__() == 2):
            output += (self.outputString[0] + ". " + self.outputString[1])
        else:
            output += ' '.join(i for i in self.outputString)
        return output

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',0,(100,25),(0,0),0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,(0,0),(4,200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',0,(150,25),(3,220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,(0,0),(0,0),1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',0,(120,30),(0,0),600)
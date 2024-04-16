class Wagon:
    def __init__(self, number):
        if type(number) == int and number >0 :
            self.number = number
        
        else:
            raise TypeError(f"can't be a " + str(type(number)) + " only 'int' or> 0" ) 

    def __str__(self):
        return f"[{self.number:^9}]"
    def __repr__(self):
        return self.__str__()

class Train:
    def __init__(self):
        self.wagons = []
    def addWagon(self,wagon):
        self.wagons.append(wagon)
        
    def __str__(self):
        for i in range(len(self.wagons)):

            return f"{self.wagons[0]} {self.wagons[1]}"
          
                  
      

train = Train()
train.addWagon(Wagon(10))
train.addWagon(Wagon(20))

print(train)
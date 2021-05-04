class Employee(): # it inherits from user class
    def __init__(self , name , userName , password , nationalcode , salary):
        self.salary = salary
        self.name = name
        super().__init__(userName , password , nationalcode)


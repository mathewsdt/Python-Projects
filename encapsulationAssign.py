

class protected: # created class named protected
    def __init__(self): # declared a function and created an instance to be called
        self.__privateVar = 10 # set a private variable with a value of 10

    def __init__(self)# declared a function and created an instance to be call
        self.__protectedVar = 92 # set a protected variable with a value of 92

obj = Protected()
obj._protectedVar = 100 # modified my protected variable with a value of 100 within class
print(self.privateVar) # used print method to display my private variable

class Protected: # created class named it Protected
    def __init__(self): #declared a function and created an instance to be called
        self._protectedVar = 0 #set a protected variable with a value of 0
        self.__privateVar = 28 #set a private variable with a value of 28

    def getPrivate(self): #declared a function called getPrivate
        print(self.__privateVar) # used print method to display private variable

    
        
obj = Protected()
obj._protectedVar = 21 # changed value of protected variable and used Obj to retrive that data
print(obj._protectedVar) # used print method to display new value of protected variable
obj.getPrivate()


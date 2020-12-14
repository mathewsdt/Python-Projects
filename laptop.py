from abc import ABC, abstractmethod #imported module abstactmethod
class laptop(ABC):#created laptop class inheriting from ABC module
    def purchase(self, amount):
        print("Your purchase amount: ",amount)

    @abstractmethod 
    def payment(self,amount):
        pass # passing argument


class VoucherPayment(laptop): # created subclass that will inherit from parent class laptop
    def payment(self,amount):
        print('Your purchase amount of {} is covered by $200 vocher '.format(amount))

obj = VoucherPayment()
obj.purchase("$100")
obj.payment("$100")

from abc import ABC, abstractmethod
class laptop(ABC):
    def purchase(self, amount):
        print("Your purchase amount: ",amount)

    @abstractedmethod
    def payment(self,amount):
        pass


class VoucherPayment(laptop):
    def payment(self,amount):
        print('Your purchase amount of {} is covered by $200 vocher '.format(amount))

obj = VoucherPayment()
obj.purchase("$100")
obj.payment("$100")

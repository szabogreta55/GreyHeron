from abc import abstractmethod

class Product():
    def __init__(self, product_name, price) -> None:
        self._product_name = product_name
        self._price = price
    
    @abstractmethod
    def get_name():
        pass

    @abstractmethod
    def get_price():
        pass
    
    # def set_price(self, x):


class Electoronics(Product):
    def __init__(self, product_name, price) -> None:
        super().__init__(product_name, price)
    
    def get_name(self):
        return self._product_name
    
    def get_price(self):
        return self._price

class Groceries(Product):
    def __init__(self, product_name, price) -> None:
        super().__init__(product_name, price)
    
    def get_name(self):
        return self._product_name
    
    def get_price(self):
        return self._price

class Clothing(Product):
    def __init__(self, product_name, price) -> None:
        super().__init__(product_name, price)
    
    def get_name(self):
        return self._product_name
    
    def get_price(self):
        return self._price

class Customer():
    def __init__(self, custonmer_name, shopping_cart) -> None:
        self.customer_name = custonmer_name
        self.shopping_cart = shopping_cart
    
class RegularCustomer(Customer):
    def __init__(self, custonmer_name, shopping_cart) -> None:
        super().__init__(custonmer_name, shopping_cart)
    
    def get_discounted_price(self):
        total = 0
        for item in self.shopping_cart:
            total += item.get_price()
        return total
    
class VIPCustomer(Customer):
    def __init__(self, custonmer_name, shopping_cart) -> None:
        super().__init__(custonmer_name, shopping_cart)
    
    def get_discounted_price(self):
        total = 0
        for item in self.shopping_cart:
            total += item.get_price()
        return total * 0.90
    

mobile = Electoronics("Samsung_phone", 100)
jeans = Clothing("blue jeans", 50)
milk = Groceries("milk", 2)

Ekene = RegularCustomer("Ekene", [mobile, jeans, milk])

Greti = VIPCustomer("Greti", [mobile, jeans, milk])

print(Ekene.get_discounted_price())
print(Greti.get_discounted_price())
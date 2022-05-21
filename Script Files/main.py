import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        assert price >= 0, f"Price {price} is not non-negative"
        assert quantity >= 0, f"Quantity {quantity} is not non-negative"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    def calculate_total_price(self, x, y):
        return x*y
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get("name"),
                # price and quantity are passed in as strings
                price = float(item.get("price")),
                quantity = int(item.get("quantity"))
            )
    
    @staticmethod
    # static method does not take in class or instance as first arg
    # similar to a normal function defined in python
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

# new Phone class
class Phone(Item):
    def __init__(self, name:str, price:float, quantity = 0, broken_phones = 0):
        # call to super function to have access to all attributes
        super().__init__(
            name, price, quantity
        )
        
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not non-negative"
        self.broken_phones = broken_phones

phone1 = Phone("jscPhonev10", 500, 5, 1)
print(Item.all)
print(Phone.all)
from item import Item

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
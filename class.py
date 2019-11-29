'''Write a class called Product. The class should have fields called name, amount, and price,
holding the product’s name, the number of items of that product in stock, and the regular
price of the product.
There should be a method get_price that receives the number of
items to be bought and returns the cost of buying that many items, where the regular price
is charged for orders of less than 10 items, a 10% discount is applied for orders of between
10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should
also be a method called make_purchase that receives the number of items to be bought and
decreases amount by that much.'''

class Product:
    def __init__(self,name,amount,price):
        self.name = name
        self.amount = amount
        self.price = price
    
    
    def get_price(self,qty):
        self.qty = qty
        if self.qty <= 10:
            return self.qty * self.price
        elif self.qty > 10 and self.qty <=99:
            return (self.qty * self.price) * 0.1
        elif self.qty > 100:
            return (self.qty * self.price) * 0.2

    def make_purchase(self,qty):
        #self.qty = qty
        remaining_item = self.amount - self.qty
        return remaining_item
quty = int(input('Enter the number of quantity you are buying: '))
name = input('Enter the name of product: ')
c = Product(name,100,70)
Price = c.get_price(quty)
whats_left = c.make_purchase(quty)
print(Price)
print(whats_left)
        

class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status='for sale'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self, tax):
        full_price = self.price + (self.price * tax)
        return full_price
    def return_reason(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0.00
        elif reason == 'like new':
            self.status = 'for sale'
        elif reason == 'opened':
            self.status = 'used'
            self.price = round(0.80 * self.price,2)
        return self
    def display_info(self):
        print 'Item Name: ' + self.item_name
        print 'Brand: ' + self.brand
        print 'Status: ' + self.status
        print 'Price: ' + str(self.price)
        print 'Cost: ' + str(self.cost)
        print 'Weight: ' + self.weight
        return self

PRODUCT1 = Product(5.99, 'Desk Fan', '.1 lbs', 'iMBAPrice', 0.99)

PRODUCT1.display_info()
print '-----RETURNED-----'
PRODUCT1.sell().add_tax(0.1)
PRODUCT1.return_reason('defective').display_info()

print ''

PRODUCT2 = Product(6.99, 'Better Desk Fan', '.2 lbs', 'iMBAPrice', 1.49)

PRODUCT2.display_info()
print '-----RETURNED-----'
PRODUCT2.sell().add_tax(0.1)
PRODUCT2.return_reason('like new').display_info()

print ''

PRODUCT3 = Product(10.99, 'Best Desk Fan', '.4 lbs', 'iMBAPrice', 1.99)

PRODUCT3.display_info()
print '-----RETURNED-----'
PRODUCT3.sell().add_tax(0.1)
PRODUCT3.return_reason('opened').display_info()

print ''

PRODUCT4 = Product(10.99, 'God-Like Desk Fan', '.4 lbs', 'iMBAPrice', 1.99)

PRODUCT4.display_info()
print '-----RETURNED-----'
PRODUCT4.sell().add_tax(0.1)
PRODUCT4.return_reason('defective').display_info()

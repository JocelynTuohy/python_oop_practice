class Store(object):
    def __init__(
            self,
            products,
            location,
            owner,
            store_name
        ):
        self.products = products
        self.location = location
        self.owner = owner
        self.store_name = store_name
    def add_product(self, product):
        self.products.append(product)
        return self
    def remove_product(self, product):
        self.products.pop(self.products.index(product))
        return self
    def inventory(self):
        print str(self.store_name) + ' Inventory:'
        for product in range(0, len(self.products)):
            print (xstr(self.products[product].quantity) + ' ' +
                   xstr(self.products[product].color) + ' ' +
                   xstr(self.products[product].brand) + ' ' +
                   xstr(self.products[product].model) + 's (' +
                   xstr(self.products[product].category) + ')')
        return self

class Product(object):
    def __init__(self, brand, category, quantity, model="", color=""):
        self.brand = brand
        self.category = category
        self.quantity = quantity
        self.model = model
        self.color = color

def xstr(s):
    return '' if s is None else str(s)

# Create products
PILOT_METROPOLITAN_ORANGE = Product('Pilot', 'fountain pen', 200,
                                    'Metropolitan', 'orange')
ROBERT_OSTER_BRONZE = Product('Robert Oster', 'ink', 500, 'Bottle', 'Bronze')
RHODIA_WEBNOTEBOOK_ORANGE = Product('Rhodia', 'paper', 400, 'webnotebook',
                                    'orange')
BAG_OF_HOLDING = Product('ThinkGeek', 'bag', 0, 'Bag of Holding', 'grey')
MELTING_CLOCK = Product('ThinkGeek', 'office', 300, 'Melting Clock', 'silver')
DARTH_VADER_MUG = Product('Disney', 'dining', 500, 'Darth Vader Mug', 'black')
FAN = Product('iMDBPrice', 'electronics', 3942, 'Metal Desk Fan', 'black')
TOMBOW_MARKERS_YELLOW = Product('Tombow', 'art supplies', 931,
                                'Dual Brush Pen', 'yellow')
CSHARP_BOOKS = Product('Wiley', 'book', 839, 'Intro to C#', 'white')
COMPUTERS = Product('Dell', 'laptop', 233, 'Latitude', 'black')


# Create 
GOULET_PEN_COMPANY = Store([PILOT_METROPOLITAN_ORANGE,
                            ROBERT_OSTER_BRONZE,
                            RHODIA_WEBNOTEBOOK_ORANGE],
                           'Virginia', 'Brian Goulet',
                           'The Goulet Pen Company')
THINKGEEK = Store([BAG_OF_HOLDING, MELTING_CLOCK, DARTH_VADER_MUG],
                  'La La Land', 'Mystery Man', 'ThinkGeek')
AMAZON = Store([FAN, TOMBOW_MARKERS_YELLOW, CSHARP_BOOKS, COMPUTERS],
               'Seattle', "Amazon's CEO", 'Amazon')

GOULET_PEN_COMPANY.inventory()
THINKGEEK.inventory()
AMAZON.inventory()

GOULET_PEN_COMPANY.remove_product(ROBERT_OSTER_BRONZE)
GOULET_PEN_COMPANY.inventory()
GOULET_PEN_COMPANY.add_product(ROBERT_OSTER_BRONZE)
GOULET_PEN_COMPANY.inventory()

THINKGEEK.add_product(PILOT_METROPOLITAN_ORANGE)
THINKGEEK.inventory()
THINKGEEK.remove_product(BAG_OF_HOLDING)
THINKGEEK.inventory()

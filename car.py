class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    def display_all(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + self.speed
        print 'Fuel: ' + self.fuel
        print 'Mileage: ' + self.mileage
        print 'Tax: ' + str(self.tax)
        return self

CAR1 = Car(50000, '100mph', 'Full', '50mpg')
CAR2 = Car(2000, '50mph', 'Mystery Amount', '30mpg')
CAR3 = Car(10000, '5mph', 'Half Full', '30mpg')
CAR4 = Car(1000, '1mph', 'Almost Empty', '5mpg')
CAR5 = Car(40000, '150mph', 'Full', '150mpg')
CAR6 = Car(20000, '70mpg', 'Mostly Full', '90mpg')

# Bike Assignment (Coding Dojo)

# Create a new class called Bike with the following properties/attributes:

# price
# max_speed
# miles
# Create 3 instances of the Bike class.

# Use the __init__() function to specify the price and max_speed of each
# instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the
# code so that the initial miles is set to be 0 whenever a new instance is
# created.

# Add the following functions to this class:

# displayInfo() - have this method display the bike's price, maximum speed, and
# # the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles
# # ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total
# # miles ridden by 5...

# Have the first instance ride three times, reverse once and have it
# displayInfo(). Have the second instance ride twice, reverse twice and have it
# displayInfo(). Have the third instance reverse three times and displayInfo().
# What would you do to prevent the instance from having negative miles?
# Which methods can return self in order to allow chaining methods?

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def display_info(self):
        print ('Price is $' + str(self.price) + '. Maximum speed is ' +
               self.max_speed + '. It has been ridden ' + str(self.miles) +
               ' miles so far.')
        return self
    def ride(self):
        print 'Riding!'
        self.miles += 10
        return self
    def reverse(self):
        print 'Reversing!'
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

BIKE1 = Bike(150, '20mph')
BIKE2 = Bike(200, '25mph')
BIKE3 = Bike(1000, '100mph')

BIKE1.ride().ride().ride().reverse().display_info()
BIKE2.ride().ride().reverse().reverse().display_info()
BIKE3.reverse().reverse().reverse().display_info()

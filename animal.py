# Define Animal class.
class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print self.name, 'current health:', str(self.health)
        return self

# Define Dog class
class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name=name, health=health)
    def pet(self):
        self.health += 5
        return self

# Define Dragon class
class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name=name, health=health)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print 'I am a Dragon'
        return self


# Create an instance of the Animal, have it walk() three times, run() twice, and
# finally displayHealth() to confirm that the health attribute has changed.
my_kitten = Animal('Thursday Next', 200)
my_kitten.walk().walk().walk().run().run().displayHealth()

# Have the Dog walk() three times, run() twice, pet() once, and have it
# displayhealth().
my_dawg = Dog('MYDAWG')
my_dawg.walk().walk().walk().run().run().pet().displayHealth()

petes_dragon = Dragon('Elliot')
petes_dragon.walk().run().fly().displayHealth()

my_cat = Animal('Kathryn Janeway', 100)
my_cat.walk().walk().run().run().run().run().displayHealth()
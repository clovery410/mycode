current_year = 2013

class Animal(object):
    def __init__(self):
        self.is_alive = True

class Pet(Animal):
    def __init__(self, name, year_of_birth, owner=None):
        Animal.__init__(self)
        self.name = name
        self.age = current_year - year_of_birth
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print("...")

class Dog(Pet):
    def __init__(self, name, yob, owner, color):
        Pet.__init__(self, name, yob, owner)
        self.color = color
    def talk(self):
        print("Woof!")

class Cat(Pet):
    def __init__(self, name, yob, owner, lives=9):
        Pet.__init__(self, name, yob, owner)
        self.lives = lives
    def talk(self):
        """A cat says 'Meow!' when asked to talk."""
        print("Meow!")
    def lose_life(self):
        if self.lives > 0:
            self.lives = self.lives - 1
            if self.lives == 0:
                self.is_alive = Flase
        else:
            print(self.name + " is not alive anymore...")

class NoisyCat(Cat):
    """A class that behaves just like a Cat, but always repeatd things twice."""
    def __init__(self, name, yob, owner, lives=9):
        Cat.__init__(self, name, yob, owner, lives)
        
    def talk(self):
        """A NoisyCat will always repeat what he/she said twice."""
        Cat.talk(self)
        Cat.talk(self)

if __name__ == "__main__":
    fido = Dog('Fido', 1993, 'Joe', 'golden')
    clifford = Dog('Clifford', 1963, 'Emily', 'red')
    print(fido.age)
    fido.talk()
    print(fido.owner)
    print(clifford.owner)
    print(clifford.color)
    clifford.eat('bone')
    lazy = Cat('Lazy', 2000, 'Clover')
    print(lazy.age)
    lazy.talk()
    print(lazy.owner)
    lazy.lose_life()
    lazy.lose_life()
    lazy.lose_life()
    lazy.lose_life()
    lazy.lose_life()
    lazy.lose_life()
    lazy.lose_life()
    lazy.lose_life()
    lazy.lose_life()
    lazy.lose_life()
    print(lazy.is_alive)
    print(lazy.lives)
    huahua = NoisyCat('Huahua', 1999, 'Ying')
    huahua.talk()

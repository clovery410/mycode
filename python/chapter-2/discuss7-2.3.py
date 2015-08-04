class Skittle(object):
    """A Skittle object has a color to describe it."""
    def __init__(self, color):
        self.color = color

class Bag(object):
    """A Bag is a collection of skittles. All bags share the number of Bags ever made (sold) and each bag keeps track of its skittles in a list.
    """
    number_sold = 0
    def __init__(self):
        self.skittles = ()
        Bag.number_sold += 1
    
    def tag_line(self):
        """Print the Skittles tag line."""
        print("Taste the rainbow!")

    def print_bag(self):
        print(tuple(s.color for s in self.skittles))

    def take_skittle(self):
        """Take the first skittle in the bag (from the front of the skittles list)."""
        skittle_to_eat = self.skittles[0]
        self.skittles = self.skittles[1:]
        return skittle_to_eat

    def add_skittle(self, s):
        """Add a skittle to the bag."""
        self.skittles += (s,)

    def take_color(self, color):
        #color_to_take = self.skittles[i]
        #self.skittles = self.skittles[:i] + self.skittles[i+1:]
        for i in range(len(self.skittles)):
            if self.skittles[i].color == color:
                color_to_take = self.skittles[i]
                self.skittles = self.skittles[:i] + self.skittles[i+1:]
                return color_to_take
        return None
        
    def take_all(self):
        while self.skittles:
            skittle_to_take = self.skittles[0]
            print(skittle_to_take.color)
            self.skittles = self.skittles[1:]

if __name__ == '__main__':
    bag = Bag()
    bag.add_skittle(Skittle('red'))
    bag.add_skittle(Skittle('green'))
    bag.add_skittle(Skittle('blue'))
    bag.add_skittle(Skittle('red'))
    bag.add_skittle(Skittle('yellow'))
    bag.add_skittle(Skittle('green'))

    print bag.take_color('blue').color
    bag.print_bag()
    bag.take_all()
    bag.print_bag()

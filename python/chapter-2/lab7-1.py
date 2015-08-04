class Person(object):
    # """
    # >>> john = Person("John")
    # >>> john.repeat()
    # "I squirreled it away before it could catch on fire."
    # >>> john.say("Hello")
    # "Hello"
    # >>> john.repeat()
    # "Hello"
    # >>> john.greet()
    # "Hello, my name is John"
    # >>> john.repeat()
    # "Hello, my name is John"
    # >>> john.ask("preserve abstraction barriers")
    # "Would you please preserve abstraction barriers"
    # >>> john.repeat()
    # "Would you please preserve abstraction barriers"
    # >>> steven = DoubleTalker("Steven")
    # steven.say("hello")
    # "hello hello"
    # >>> steven.say(the sky is falling")
    # "the sky is falling the sky is falling"
    # """
    def __init__(self, name):
        self.name = name
        self.previous = "I squirreled it away before it could catch on fire."

    def say(self, stuff):
        self.previous = stuff
        return stuff

    def ask(self, stuff):
        #self.previous = self.say("Would you please " + stuff)
        return self.say("Would you please " + stuff)

    def greet(self):
        #self.previous = self.say("Hello, my name is " + self.name)
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        return self.previous

class DoubleTalker(Person):
    """
    >>> steven = DoubleTalker("Steven")
    >>> steven.say("hello")
    "hello hello"
    >>> steven.say("the sky is falling")
    "the sky is falling the sky is falling"
    """
    def __init__(self, name):
        Person.__init__(self, name)
    def say(self, stuff):
        return Person.say(self, stuff + " " + stuff)

if __name__ == "__main__":
    steven = DoubleTalker("Steven")
    print(steven.say("hello"))
    print(steven.repeat())
    print(steven.say("the sky is falling"))

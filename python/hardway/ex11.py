print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
a = int(raw_input("Input first number:"))
b = int(raw_input("Input second number:"))
print "So, you're %r old, %r tall and %r heavy. Total is %d" % (
    age, height, weight, a+b)

name = raw_input("What's your name: ")
state = raw_input("Where are you from: ")
phone = raw_input("What's your phone number: ")

print "Your name is %s, from %s, and phone number is %s, right?" % (
    name, state, phone)

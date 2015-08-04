# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print "You have %d cheeses!" % cheese_count
#     print "You have %d boxes of crackers!" % boxes_of_crackers
#     print "Man that's enough for a party!"
#     print "Get a blanket.\n"

# print "We can just give the function numbers directly:"
# cheese_and_crackers(20, 30)

# print "OR, we can use variables from our script:"
# amount_of_cheese = 10
# amount_of_crackers = 50

# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print "We can even do math inside too:"
# cheese_and_crackers(10 + 20, 5 + 6)

# print "And we can combine the two, variables and math:"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

from sys import argv

def apple_and_oranges(apple_count, orange_count):
    print "Now you have %d apples and %d oranges." % (apple_count, orange_count)

buy_apple = int(raw_input("How many apples would you buy? "))
buy_orange = int(raw_input("How many oranges would you buy? "))

current_apple = 2
current_orange = 3

apple_and_oranges(current_apple + buy_apple, current_orange + buy_orange)

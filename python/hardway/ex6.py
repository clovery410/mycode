x = "There are %d types of people." % 10  # make definition of variable x
binary = "binary" # make definition of variable binary
do_not = "don't" # make definition of variable do_not
y = "Those who know %s and those who %s." % (binary, do_not) # make definition of variable y

print x # print x
print y # print y

print "I said: %r." % x # print a string with variable x
print "I also said: '%s'." % y # print a string with variable y

hilarious = False # assign variable hilarious with the value of False
joke_evaluation = "Isn't that joke so funny?! %r" # assign variable joke_evaluation a string

print joke_evaluation % hilarious # print string joke_evaluation

w = "This is the left side of..." # assign variable w with a string value
e = "a string with a right side." # assign variable e with a string value

print w + e # print string

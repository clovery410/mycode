# i = 0
# numbers = []
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i


def accumulate(num, j):
    i = 0
    numbers = []
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + j
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

def accum_for(num):
    i = 0
    numbers = []
    for i in range(0, num):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % (i + 1)
    return numbers

#numbers = accumulate(6, 2)
numbers = accum_for(6)

print "The numbers: "

for num in numbers:
    print num

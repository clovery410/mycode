import random
f = open('test.txt', 'w')
for i in xrange(10000):
    f.write(str(random.randint(1, 999)))
    f.write('\n')




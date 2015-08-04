f = open('knapsack1.txt')

content = f.read()
lines = content.splitlines()

size = int(lines[0].split()[0])
num_items = int(lines[0].split()[1])

items = list()
optimal = list()
cache = {}

for line in lines[1:]:
    value = int(line.split()[0])
    weight = int(line.split()[1])
    items.append([value, weight])

a = [[0 for x in range(size + 1)] for x in range(num_items + 1)]

for i in range(1, num_items + 1):
    for x in range(size + 1):
        if items[i - 1][1] <= x:
            a[i][x] = max(a[i - 1][x], a[i - 1][x - items[i - 1][1]] + items[i - 1][0])
        else:
            a[i][x] = a[i - 1][x]

print(a[num_items][size])

while a[i][x] > 0:
    if a[i][x] == a[i - 1][x]:
        i = i - 1
    else:
        optimal.append([items[i - 1][0], items[i - 1][1]])
        i = i - 1
        x = x - items[i - 1][1]

optimal.reverse()
print(optimal)
    

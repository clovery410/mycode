import sys
sys.setrecursionlimit(3000)

knap_memo = {}

def knap_recursive(i, x):
    if i <= 0:
        return 0
    w = items[i - 1][1]
    v = items[i - 1][0]
    if (i, x) in knap_memo:
        return knap_memo[(i, x)]
    if x < w:
        result = knap_recursive(i - 1, x)
        knap_memo[(i, x)] = result
        return result
    else:
        result = max(knap_recursive(i - 1, x), knap_recursive(i - 1, x - w) + v)
        knap_memo[(i, x)] = result
        return result
            
f = open('knapsack_big.txt')

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

result = knap_recursive(num_items, size)
print(result)
# #2-D array
# # a = [[0 for x in range(size + 1)] for x in range(num_items + 1)]

# #2*W
# a = [[0 for x in range(size + 1)] for x in range(2)]

# for i in range(1, num_items + 1):
#     for x in range(size + 1):
#         if items[i - 1][1] <= x:
#             a[1][x] = max(a[0][x], a[0][x - items[i - 1][1]] + items[i - 1][0])
#         else:
#             a[1][x] = a[0][x]
#     for element in range(x + 1):
#         a[0][element] = a[1][element]
#     print('Current item number: %s' % i)

# print(a[0][x])

# while a[i][x] > 0:
#     if a[i][x] == a[i - 1][x]:
#         i = i - 1
#     else:
#         optimal.append([items[i - 1][0], items[i - 1][1]])
#         i = i - 1
#         x = x - items[i - 1][1]

# optimal.reverse()
# print(optimal)
 

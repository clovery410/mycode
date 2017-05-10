import operator

f = open('percent04mid.csv')

content = f.read()
lines = content.splitlines()

stock_union = {}

for line in lines:
    stock_code = str(line.split(',')[0])
    p1 = float(line.split(',')[1])
    p2 = float(line.split(',')[2])
    stock_union[stock_code] = [p1, p2]

print(stock_union)

f = open('output_2004mid.txt')

content = f.read()
lines = content.splitlines()

data = {}

for line in lines:
    stock_code = str(line.split()[0])
    intimes = int(line.split()[1])
    outtimes = int(line.split()[2])
    toltimes = int(line.split()[3])
    data[stock_code] = [intimes, outtimes, toltimes]

print(data)

for item in data:
    percent1 = stock_union[item][0]
    percent2 = stock_union[item][1]
    data[item].append(percent1)
    data[item].append(percent2)

print(data)

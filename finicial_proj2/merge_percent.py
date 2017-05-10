import operator

f = open('percent05end.csv')

content = f.read()
lines = content.splitlines()

stock_union = {}

for line in lines:
    stock_code = str(line.split(',')[0])
    p1 = float(line.split(',')[1])
    p2 = float(line.split(',')[2])
    stock_union[stock_code] = [p1, p2]

print(stock_union)

f = open('output_2005end.txt')

content = f.read()
lines = content.splitlines()

merge_data = list()

for line in lines:
    stock_code = str(line.split()[0])
    intimes = int(line.split()[1])
    outtimes = int(line.split()[2])
    toltimes = int(line.split()[3])
    if stock_code in stock_union:
        percent1 = stock_union[stock_code][0]
        percent2 = stock_union[stock_code][1]
        merge_data.append([stock_code, intimes, outtimes, toltimes, percent1, percent2])
    else:
        merge_data.append([stock_code, intimes, outtimes, toltimes, 'delist'])

merge_data = sorted(merge_data, key = operator.itemgetter(3), reverse = True)

f = open('2005end.txt', 'w')
f.writelines("%s\n" % ' '.join([str(i) for i in item]) for item in merge_data)

print(merge_data)

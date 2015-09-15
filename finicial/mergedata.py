import operator

f = open('in2004mid.txt')

content = f.read()
lines = content.splitlines()

in_size = int(lines[0])

in_result = {}

for line in lines[1:]:
    stock_code = str(line)
    if not stock_code in in_result:
        in_result[stock_code] = 1

    else:
        in_result[stock_code] += 1

#print(in_result)

f = open('out2004mid.txt')

content = f.read()
lines = content.splitlines()

out_size = int(lines[0])

out_result = {}

for line in lines[1:]:
    stock_code = str(line)
    if not stock_code in out_result:
        out_result[stock_code] = 1
    else:
        out_result[stock_code] += 1

#print(out_result)

merge_data = list()

for item in in_result:
    in_trade = in_result[item]
    if item in out_result:
        out_trade = out_result[item]
        sum_trade = in_trade + out_trade
        merge_data.append([item, in_trade, out_trade, sum_trade])
    else:
        merge_data.append([item, in_trade, 0, in_trade])

for item in out_result:
    if item not in in_result:
        out_trade = out_result[item]
        merge_data.append([item, 0, out_trade, out_trade])

merge_data = sorted(merge_data, key = operator.itemgetter(3), reverse = True)
#print(merge_data)

f = open('output.txt', 'w')
#f.writelines(' '.join([str(i) for i in item]) for item in merge_data)
f.writelines("%s\n" % ' '.join([str(i) for i in item]) for item in merge_data)

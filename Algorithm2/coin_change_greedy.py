optimal = {}

def greedy_change(total, choice):
    if total == 0:
        return
#    import pdb
#    pdb.set_trace()
    if total / choice[0] > 0:
        print('%s ' % choice[0])
        return greedy_change(total - choice[0], choice)
    elif total / choice[1] > 0:
        print('%s ' % choice[1])
        return greedy_change(total - choice[1], choice)
    else:
        print('%s ' % choice[2])
        return greedy_change(total - choice[2], choice)

best_solution = list()
def dp_change(total, choice):
    if total <= 0:
        return 0
    if total / choice[0] <= 0:
        return dp_change(total, choice[1:])
    elif (len(choice) > 1):
         count_withFirst = dp_change(total - choice[0], choice) + 1
         count_withoutFirst = dp_change(total, choice[1:])
         if count_withFirst <= count_withoutFirst:
              return count_withFirst
         else:
             return count_withoutFirst
    if (len(choice) == 1):
        count = 1 + dp_change(total - choice[0], choice)
        return count

c = {}
def new_dp_change(total, choices):
    min_count = 9999
    if total == 0:
        return 0
    for coin in choices:
        if total < coin:
            continue
        else:
            count = new_dp_change(total - coin, choices)
            if count < min_count:
                min_count = count
                c[total] = coin
    return min_count + 1

            
    
    
if __name__ == '__main__':
#    total_money = 8
    choice = [7, 6, 5, 4, 1]

    for total_money in range(1, 1000):
        print total_money
        if dp_change(total_money, choice) != new_dp_change(total_money, choice):
            print('value %s is different' % i)
#    greedy_change(total_money, choice)
#    num = dp_change(total_money, choice)
#    num = new_dp_change(total_money, choice)
#    print(num)
#    print(c)

    # while total_money > 0:
    #     print(c[total_money])
    #     total_money  = total_money - c[total_money]

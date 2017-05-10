#solution1, wrong solution...
def nonDominatable():
    n = int(raw_input("Enter how many pairs:"))
    res = 0
    min_x, min_y, max_x, max_y = None, None, None, None
    for i in range(n):
        cur_line = raw_input("enter current pair:").split(" ")
        cur_x, cur_y = int(cur_line[0]), int(cur_line[1])
        if min_x == min_y == None:
            min_x = max_x = cur_x
            min_y = max_y = cur_y
        else:
            if cur_x > max_x and cur_y > max_y:
                min_x = max_x = cur_x
                min_y = max_y = cur_y
                res = i
            elif cur_x < min_x and cur_y < min_y:
                res += 1
            else:
                if cur_x > max_x: max_x = cur_x
                if cur_y > max_y: max_y = cur_y
    return n - res

#solution2, correct solution
def nonDominatable2():
    n = int(raw_input("Enter how many pairs:"))
    res = 1
    timeline = []

    for i in range(n):
        cur_line = raw_input("Enter current pair:").split(" ")
        cur_x, cur_y = int(cur_line[0]), int(cur_line[1])
        timeline.append((cur_x, cur_y))
    timeline.sort(key = lambda x: (x[1], -x[0]))
    
    target_x = timeline[-1][0]
    for i in reversed(range(n-1)):
        if timeline[i][0] >= target_x:
            res += 1
            target_x = timeline[i][0]
    return res

if __name__ == "__main__":
    print nonDominatable()
    

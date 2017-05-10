def coin_change(amount, coins):
    """
    coins = [1, 2, 5, 10, 50, 100]
    amount = 6
    should return [[1,1,1,1,1,1], [1,1,1,1,2], [1,1,2,2], [2,2,2], [1,5]]
    """
    def helper(idx, total, curr_solution, all_solutions):
        if idx >= len(coins):
            if total == amount:
                all_solutions.append(curr_solution[:])
            return
        if total == amount:
            all_solutions.append(curr_solution[:])
            return

        #do not choose current coin
        helper(idx, total, curr_solution, all_solutions)

        #choose current coin
        curr_solution.append(coin[idx])
        helper(idx, total + coin[idx], curr_solution, all_solutions)
        helper(idx + 1 ,total + coin[idx], curr_solution, all_solutions)
        curr_solution.pop()

    res = []
    helper(0, 0, [], res)
    return res

if __name__ == '__main__':
    print coin_change(6, [1, 2, 5])

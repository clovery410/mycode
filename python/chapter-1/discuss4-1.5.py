#1.5 Now write sum_filter_up_to(n, pred), which is a general version that adds all integers 1 through n that satisfy the argument pred.
def sum_filter_up_to(n, pred):
    if n == 0:
        return 0
    elif pred(n):
        return sum_filter_up_to(n - 1, pred) + n
    else:
        return sum_filter_up_to(n - 1, pred)

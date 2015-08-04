"""1. Now implement the function every that takes in a function func and a number n, and applies that function to the first n numbers from 1 and prints the result along the way:"""
def every(func, n):
    x = 1
    while x <= n:
        print(func(x))
        x += 1

"""2. Similarly, implement the function keep, which takes in a function condition cond and a number n, and only prints a number from 1 to n to the screen if it fulfills the condition:"""
def keep(cond, n):
    x = 1
    while x <= n:
        if cond(x):
            print(x)
        x += 1

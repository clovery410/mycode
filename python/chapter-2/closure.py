def function():
    private = {'MY_CONST': '1', 'ANOTHER_CONST': '2'}
    return lambda name: private[name]

config = function()


if __name__ == "__main__":
    print(config('MY_CONST'))
#    config('MY_CONST') = 2
    print(config('MY_CONST'))

print('aaa')
def get_counter():
    i = 0
    def increment():
        nonlocal i  # make i writable
        i = i + 1
        return i
    return increment
print('bbb')

counter1 = get_counter()
counter2 = get_counter()
print(counter1())
print(counter2())
print(counter1())
_counter = 0
print(counter2())
print(counter1())


_counter = 0

def counter():
    global _counter
    _counter = _counter + 1
    return _counter
print ('---------------------')
print (counter())
_counter = 0
print (counter())
print (counter())


    

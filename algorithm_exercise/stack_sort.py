# Sort the element in the stack, only use pop(), top(), push(), isEmpty(), isFull()
def isEmpty(s):
    if len(s) == 0:
        return True
    return False

def top(s):
    return s[-1]

def sort_stack(s):
    dest = []
    while not isEmpty(s):
        candidate = s.pop()
        if isEmpty(dest) or candidate >= top(dest):
            dest.append(candidate)
        else:
            temp = []
            while not isEmpty(dest) and top(dest) > candidate:
                temp.append(dest.pop())
            dest.append(candidate)
            while not isEmpty(temp):
                dest.append(temp.pop())

    s[:] = dest

s = [2,3,1,4,6,5]
sort_stack(s)
print s
        

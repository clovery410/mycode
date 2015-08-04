def zero(f):
    return lambda x: x # Identity function

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

one = successor(zero)
two = successor(one)
three = successor(two)

#     = lambda f: lambda x: f(zero(f)(x))
#     = lambda f: lambda x: f(lambda y: y (x))
#     = lambda f: lambda x: f(x)

# def one(f):
#     return lambda x: f(x)

# two = successor(one)
#     = lambda f: lambda x: f(one(f)(x))
#     = lambda f: lambda x: f((lambda y: f(y))(x))
#     = lambda f: lambda x: f(f(x))

def sum(n, m):
    return lambda f: lambda x: m(f)(n(f)(x))

    # n = one, m = two
    # = lambda f: lambda x: two(f)(one(f)(x))
    # = lambda f: lambda x: two(f)(f(x))
    # = lambda f: lambda x: (lambda y: f(f(y)))(f(x))
    # = lambda f: lambda x: f(f(f(x)))

    # return lambda x: f(f(...(f(x))))
    
def mul(n, m):
    return lambda f: lambda x: m(n(f))(x)

    # n = three, m = two
    # = lambda f: lambda x: two(three(f))(x)
    # = lambda f: lambda x: two(lambda y: f(f(f(y))))(x)
    # = lambda f: lambda x: (lambda z: (lambda y: f(f(f(y))))((lambda y: f(f(f(y))))(z)))(x)
    # = lambda f: lambda x: (lambda z: (three(f)(three(f)(z))(x)
    # = lambda f: lambda x: (lambda z: f(f(f(f(f(f(z)))))))(x)
    # = lambda f: lambda x: f(f(f(f(f(f(x))))))
    # = lambda x: f(f(f(f(f(f(x))))))

def pow(n, m):
    return lambda f: lambda x: m(n)(f)(x)
          
def church_to_int(n):
    return n(lambda x: x + 1)(0)

print church_to_int(one)
print church_to_int(two)
print church_to_int(three)
print church_to_int(sum(two, three))
print church_to_int(sum(three, sum(three, two)))
print church_to_int(mul(three, three))
print church_to_int(mul(three, mul(three, two)))

print church_to_int(pow(two, three))



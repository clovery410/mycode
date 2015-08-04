import inspect

t2 = lambda f: lambda x: f(f(x))
t3 = lambda f: lambda x: f(f(f(x)))
t4 = lambda f: lambda x: f(f(f(f(x))))
s = lambda x: x + 1

def function_t(f):
    def function_result(x):
        f_str = inspect.getsource(f)
        x_str = str(x) if isinstance(x, int) else inspect.getsource(x)
        _tmp = f(f(f(x)))
        print ('f(f(f(x))), f=%s, x=%s' % (f_str, x_str))
        return _tmp
    return function_result

def function_s(x):
    print ('x + 1')
    return x + 1

print(t2(t2)(s)(0))
print(t2(t3)(s)(0))
print(t3(t4)(s)(0))
print(t2(t4)(s)(0))
print(t2(t3(t4))(s)(0))
print(t3(t2(t4))(s)(0))

    

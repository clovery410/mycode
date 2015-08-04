t = lambda f: lambda x: f(f(f(x)))
s = lambda x: x + 1

#1 t(s)(0) = 3
#2 t(t(s))(0) = 9
#3 t(t)(s)(0)

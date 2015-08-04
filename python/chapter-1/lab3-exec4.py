#For each of the following expressions, what must f be in order for the evaluation of the expression to succeed, without causing an error? Give a definition of f for each expression such that evaluating the expression will not cause an error.


f = 3

f() = lambda : 3

f(3) = lambda x: x

f()() = lambda : lambda : 3

f()(3)() = lambda : lambda x: lambda : x

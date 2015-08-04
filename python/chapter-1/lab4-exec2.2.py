def sin(x):
    if abs(x) <= 0.0001:
        return x
    return 3 * sin(x / 3) - 4 * pow(sin(x / 3), 3)

print(sin(90))

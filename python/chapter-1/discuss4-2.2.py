#2.2 Pascal's triangle is a useful recursive definition that tells us the coefficients in the expansion of the polynomial (x + a)^n. Each element in the triangle has a coordinate, given by the row it is on and its position in the row(which you could call its column). Every number in Pascal's triangle is defined as the sum of the item above it and the item that is directly to the upper left of it. If there is a position that dose not have an entry, we treat it as if we had a 0 there. 
def pascal(row, column):
    if row < 0 or column < 0:
        return 0
    elif row == column:
        return 1
    elif row < column:
        return 0
    else:
        return pascal(row - 1, column - 1) + pascal(row - 1, column)

for i in range(0, 10):
    line = ''
    for j in range(0, 10):
        line += str(pascal(i, j))
        line += ' '
    print line

        

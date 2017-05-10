def cut(n, arr):
    if n > 0:
        arr.sort()
        pre = arr[0] - 1
        for i, stick in enumerate(arr):
            if stick > pre:
                print n - i
                pre = stick

if __name__ == "__main__":
    cut(6, [5, 4, 4, 2, 2, 8])

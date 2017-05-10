import sys
def mergeSort(nums, p, r):
    if p < r:
        mid = (r - p) / 2 + p
        mergeSort(nums, p, mid)
        mergeSort(nums, mid+1, r)
        merge(nums, p, mid, r)

def merge(nums, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    l1 = [sys.maxint] * (n1+1)
    l2 = [sys.maxint] * (n2+1)
    for i in xrange(n1):
        l1[i] = nums[p+i]
    for j in xrange(n2):
        l2[j] = nums[q+j+1]
    i = j = 0
    for k in xrange(p, r+1):
        if l1[i] <= l2[j]:
            nums[k] = l1[i]
            i += 1
        else:
            nums[k] = l2[j]
            j += 1

if __name__ == "__main__":
    nums = [3, 4, 6, 1, 7, 2, 5, 8]
    mergeSort(nums, 0, 7)
    print nums

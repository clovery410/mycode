def left_child(i):
    return (i + 1) * 2 - 1

def right_child(i):
    return (i + 1) * 2

def max_heapfy(nums, index, heap_size):
    while index < heap_size:
        l_index = left_child(index)
        r_index = right_child(index)
        largest = index
        if l_index < heap_size and nums[l_index] > nums[index]:
            largest = l_index
        if r_index < heap_size and nums[r_index] > nums[largest]:
            largest = r_index
        if largest == index:
            return
        else:
            nums[largest], nums[index] = nums[index], nums[largest]
            index = largest

def build_max_heap(nums):
    n = len(nums)
    for i in reversed(xrange(n/2)):
        max_heapfy(nums, i, n)

def heapsort(nums):
    n = heap_size = len(nums)
    build_max_heap(nums)

    for i in reversed(xrange(1, n)):
        nums[0], nums[i] = nums[i], nums[0]
        heap_size -= 1
        max_heapfy(nums, 0, heap_size)

def min_heapfy(nums, index, heap_size):
    while index < heap_size:
        l_index = left_child(index)
        r_index = right_child(index)
        minimum = index
        if l_index < heap_size and nums[l_index] < nums[index]:
            minimum = l_index
        if r_index < heap_size and nums[r_index] > nums[minimum]:
            minimum = r_index
        if minimum == index:
            return
        else:
            nums[minimum], nums[index] = nums[index], nums[minimum]
            index = minimum

array = []
max_heap = []
min_heap = []
def get_online_median(a):
    array.append(a)
    n = len(array)
    if n == 1:
        return a
    if n == 2:
        min_heap.append(max(array[0], array[1]))
        max_heap.append(min(array[0], array[1]))
        return (max_heap[0] + min_heap[0]) / 2

    if n % 2 == 1:
        if a <= max_heap[0]:
            max_heap.append(a)
            return max_heap[0]
        if a >= min_heap[0]:
            min_heap.append(a)
            return min_heap[0]
        else:
            max_heap.append(a)
            max_heapfy(max_heap, 0, n / 2 + 1)
            return a
    else:
        if a <= max_heap[0]:
            min_heap.append(max_heap[0])
            min_heapfy(min_heap, 0, n / 2)
            max_heap[0] = a
            max_heapfy(max_heap, 0, n / 2)
        if a >= min_heap[0]:
            min_heap.append(a)
        else:
            min_heap.append(a)
            min_heapfy(min_heap, 0, n / 2)
        return (max_heap[0] + min_heap[0]) / 2
        
    
nums = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
#heapsort(nums)

print get_online_median(4)
print get_online_median(1)
print get_online_median(3)
print get_online_median(2)
print get_online_median(16)


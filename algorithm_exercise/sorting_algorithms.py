import random
import heapq

def bubble_sort(nums):
    # each round, get the largest num in sub array all the way to the right
    for i in xrange(len(nums)):
        for j in xrange(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


def insertion_sort(nums):
    # each round, get the sub array nums[:i+1] in correct order
    for i in xrange(1, len(nums)):
        j = i
        while j > 0 and nums[j] > nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1

def merge_sort(nums):
    if len(nums) <= 1:
        return
    mid = len(nums) / 2
    left = nums[0:mid]
    right = nums[mid:]

    merge_sort(left)
    merge_sort(right)

    l, r = 0, 0
    for i in xrange(len(nums)):
        l_val = left[l] if l < len(left) else None
        r_val = right[r] if r < len(right) else None

        if (l_val is not None and r_val is not None and l_val < r_val) or r_val is None:
            nums[i] = left[l]
            l += 1
        elif (l_val is not None and r_val is not None and l_val >= r_val) or l_val is None:
            nums[i] = right[r]
            r += 1
        else:
            raise Exception('Count not merge, sub arrays size does not match')

def quick_sort(nums):
    if len(nums) > 1:
        pivot_index = len(nums) / 2
        smaller_nums = []
        larger_nums = []

        for i, val in enumerate(nums):
            if i != pivot_index:
                if val < nums[pivot_index]:
                    smaller_nums.append(val)
                else:
                    larger_nums.append(val)
        quick_sort(smaller_nums)
        quick_sort(larger_nums)
        nums[:] = smaller_nums + [nums[pivot_index]] + larger_nums

def heap_sort(nums):
    heapq.heapify(nums)
    nums[:] = [heapq.heappop(nums) for i in xrange(len(nums))]


if __name__ == "__main__":
    random_items = [random.randint(-50, 100) for x in xrange(32)]
    print 'Before: ', random_items
    heap_sort(random_items)
    print 'After: ', random_items
    

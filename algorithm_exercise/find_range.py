def getNumberRange(numbers, x):
    length = len(numbers)
    start, end = 0, length - 1

    # Find the index of any number equals to key
    while start <= end:
        mid = (start + end) / 2
        if numbers[mid] == x:
            break
        if numbers[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    if start > end:
        return [-1, -1]

    # extend numbers by 1
    numbers = [numbers[0] - 1,] + numbers + [numbers[-1] + 1,]    
    start_head, end_head = 1, mid + 1
    start_tail, end_tail = mid + 1, len(numbers) - 1
    range_start = range_end = mid + 1
    print numbers, start_head, end_head, start_tail, end_tail

    while start_head <= end_head:
        mid_head = (start_head + end_head) / 2
        if numbers[mid_head] == x and numbers[mid_head - 1] < x:
            range_start = mid_head
            break
        if numbers[mid_head] < x:
            start_head = mid_head + 1
        else:
            end_head = mid_head
            
    while start_tail <= end_tail:
        mid_tail = (start_tail + end_tail) / 2
        if numbers[mid_tail] == x and numbers[mid_tail + 1] > x:
            range_end = mid_tail
            break
        if numbers[mid_tail] > x:
            end_tail = mid_tail - 1
        else:
            start_tail = mid_tail + 1
        
    return [range_start - 1, range_end - 1]


nums = [1, 2, 4, 5, 5, 7, 7, 7, 8, 9, 9, 9, 10]
nums2 = [7, 7, 7, 7, 7, 7]
print getNumberRange(nums, 7)

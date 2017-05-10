def intersection(nums1, nums2):
    ret = []
    n1, n2 = len(nums1), len(nums2)
    i = j = 0

    while i < n1 and j < n2:
        curr_1 = nums1[i]
        curr_2 = nums2[j]
        if curr_1 == curr_2:
            ret.append(curr_1)
            i += 1
            j += 1
        else:
            if curr_1 < curr_2:
                i += 1
            else:
                j += 1

    print ret

nums1 = [1,3,5,7,9,15]
nums2 = [2,7,8,9,10,15]
intersection(nums1, nums2)

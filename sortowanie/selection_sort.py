

nums1 = [9, 4, 10, 2, 8, 5, 6, 1, 7, 3]

def selection_sort(nums):
    for i in range(len(nums)):
        p = nums[i]
        p_i = i
        for j in range(i, len(nums)):
            if nums[j] < p:
                p = nums[j]
                p_i = j
        nums[i], nums[p_i] = nums[p_i], nums[i]
    return nums
print(selection_sort(nums1))
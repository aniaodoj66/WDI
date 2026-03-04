

nums1 = [9, 4, 10, 2, 8, 5, 6, 1, 7, 3]

def insertion_sort(nums):
    for i in range(len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[j + 1] < nums[j]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(insertion_sort(nums1))
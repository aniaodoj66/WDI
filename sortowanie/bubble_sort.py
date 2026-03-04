

nums1 = [9, 4, 10, 2, 8, 5, 6, 1, 7, 3]

def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
print(bubble_sort(nums1))
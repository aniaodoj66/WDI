###########

nums1 = [9, 4, 10, 2, 8, 5, 6, 1, 7, 3]

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
def merge
print(merge_sort(nums1))
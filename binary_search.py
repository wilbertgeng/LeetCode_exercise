"""
Find a number: 69, 744
Find left bound: 540, 278, 153, 34
Find right bound:
"""

""" Find a number """
def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r-l)//2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
    return -1

""" Find left bound """
def left_bound(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        m = l + (r - l)//2
        if nums[m] >= target:
            r = m
        elif nums[m] < target:
            l = m + 1

    return l
    # what if target doesn't exist?
    return -1 if l == len(nums) else l

def left_bound(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l)//2
        if nums[m] >= target:
            r = m - 1 # 搜索区间变为 [left, mid-1]
        elif nums[m] < target:
            l = m + 1 # 搜索区间变为 [mid+1, right]

    if l >= len(nums) or nums[l] != target:
        return -1
    return l

""" Find right bound """
def right_bound(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        m = l + (r - l)//2
        if nums[m] > target:
            r = m # 搜索区间变为 [left, mid)
        elif nums[m] <= target:
            l = m + 1 # 搜索区间变为 [mid+1, right)
    if l == 0 or nums[l-1] != target: # l == len(nums) - 1 impossible l == len(nums) is considered already
        return -1
    return l - 1

def right_bound(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l)//2
        if nums[m] > target:
            r = m - 1
        elif nums[m] <= target:
            l = m + 1
    if nums[l-1] != target or right < 0: # right = left -1
        return -1
    return l - 1









#

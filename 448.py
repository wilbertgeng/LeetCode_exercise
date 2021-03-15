# Find all numbers disappeared in an Array
class Solution(object):
    def findDisappearedNumbers(self, nums):
        #"""
        #:type nums: List[int]
        #:rtype: List[int]
        #"""



        for i in range (len(nums)):
            index = abs(nums(i)) -1
            num[index]= -abs(num[index])

        return [i+1 for i in range(len(nums)) if nums[i]>0]

nums = [4,3,2,7,8,2,3,1]
print(Solution.findDisappearedNumbers())

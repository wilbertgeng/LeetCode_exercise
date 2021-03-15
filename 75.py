"""Sort Colors"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ################# Practice
        r = 0
        w = 0
        b = len(nums) - 1
        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 2:
                nums[b], nums[w] = nums[w], nums[b]
                b -= 1 ### Be careful here that White position doesn't change
            elif nums[w] == 1:
                w += 1


        ## review practice
        v0 = 0
        v1 = 0
        v2 = len(nums) - 1

        while v1 <= v2:
            if nums[v1] == 1:
                v1 += 1
            elif nums[v1] == 0:
                nums[v0], nums[v1] = nums[v1], nums[v0]
                v1 += 1
                v0 += 1
            elif nums[v1] == 2:
                nums[v1], nums[v2] = nums[v2], nums[v1]
                v2 -= 1


        ## R2:
        p0, p1, p2 = 0, 0, len(nums)-1

        while p1 < = p2:
            if nums[p1] == 0:
                nums[p1], nums[p0] = nums[p0], nums[p1]
                p1 += 1
                p0 += 1
            elif nums[p1] == 1:
                p1 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1

        return nums

        ## R1:
        r, w, b = 0, 0, len(nums)-1

        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[b], nums[w] = nums[w], nums[b]
                b -= 1

        return nums

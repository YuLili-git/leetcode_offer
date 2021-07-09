#在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
###########################solution 1########################################
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                return i
###########################solution 2########################################
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                return i

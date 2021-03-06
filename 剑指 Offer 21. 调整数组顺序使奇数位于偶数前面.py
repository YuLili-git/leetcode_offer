#输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#示例：
#输入：nums = [1,2,3,4]
#输出：[1,3,2,4] 
#注：[3,1,2,4] 也是正确的答案之一
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 != 0:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

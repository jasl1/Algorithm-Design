class Solution(object):
    def longestConsecutive(self, nums):
        
        num_set = set(nums)
        max_l = 0
        for num in num_set:
            if (num -1) not in num_set:
                temp = 1
                current = num + 1
                while current in num_set:
                    temp += 1
                    current += 1
                if temp > max_l:
                    max_l = temp
        return max_l

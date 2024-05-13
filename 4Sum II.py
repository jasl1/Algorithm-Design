import collections

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        sums = collections.defaultdict(int)
        answer = 0
        for num1 in nums1:
            for num2 in nums2:
                sum_ = -(num1 + num2)
                sums[sum_] +=1

        for num3 in nums3:
            for num4 in nums4:
                sum_ = num3 + num4
                answer += sums[sum_]
        
        return answer 

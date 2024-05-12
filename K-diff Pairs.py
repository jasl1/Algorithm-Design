class Solution(object):
    def findPairs(self, nums, k):
        answer = 0
        pairs = {}
        for y in nums:
            if y in pairs and k!=0:
                continue
            
            if k+y in pairs:
                if y not in pairs[k+y]:
                    answer += 1
                    pairs[k+y].append(y)

            if y-k in pairs:    
                if y not in pairs[y-k]:
                    answer += 1
                    pairs[y-k].append(y)

            if y not in pairs:
                pairs[y] = []
        return answer

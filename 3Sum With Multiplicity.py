class Solution(object):
    def threeSumMulti(self, arr, target):
        answer = 0
        for z in range(2,len(arr)):
            k = target - arr[z]

            nums = {arr[0]:1}

            for y in range(1,z):
                x = k - arr[y]
                if x in nums:
                    answer += nums[x]

                if arr[y] in nums:
                    nums[arr[y]] += 1
                else:
                    nums[arr[y]] = 1
            answer %=(pow(10, 9) + 7)
            del nums
        return answer

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == 0:
            ans = 1
            for i in nums:
                ans *= i
            r = []
            for number in nums:
                r.append(int(ans * (number ** -1)))
            return r
        elif nums.count(0) == 1:
            ans = 1
            r = []
            for i in nums:
                if i != 0:
                    ans *= i
                    r.append(0)
            r.insert(nums.index(0), ans)
            return r
        else:
            return [0 for i in nums]
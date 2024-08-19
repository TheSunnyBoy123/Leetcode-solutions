class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        x = set(nums)
        longest = 0

        while len(x):#picked a number
            i = x.pop()
            back = 1
            forward = 1
            while i - back in x:
                x.remove(i-back)
                back += 1
            while i + forward in x:
                x.remove(i+forward)
                forward += 1
            if forward + back - 1 > longest:
                longest = forward + back - 1
        return (longest)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        #start from right most
        picked = len(nums) - 1
        while (picked != 0):
            left = 0
            right = picked - 1
            while left < right and right > 0 and left >= 0:
                if nums[picked] + nums[left] + nums[right] == 0:
                    if sorted([nums[picked], nums[left], nums[right]]) not in ans:
                        ans.append(sorted([nums[picked], nums[left], nums[right]]))
                    left += 1
                elif nums[picked] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
            picked -= 1
        return ans
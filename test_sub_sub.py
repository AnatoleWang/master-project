class Solution:
    def searchRange(self, nums, target: int):
        n = len(nums)
        l, r = 0, n-1
        ans = [-1,-1]
        if nums[0] > target or nums[-1] < target:
            return ans
        while l <= r:
            if nums[l] == nums[r]:
                break
            if nums[l] < target:
                l += 1
            if nums[l] == target:
                ans[0] = l
            if nums[r] > target:
                r -= 1
            if nums[r] == target:
                ans[1] = r
        return ans

a = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(a.searchRange(nums,target))


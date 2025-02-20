# https://leetcode.com/problems/3sum/description/
# a generic solution for n_sum problem with any target
# optimized runtime with cache and 2-pointer solution for n=2 base case


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cache = {}

        def n_sum( n,start,target):
            key = (n,start,target)
            if key in cache:
                return cache[(n,start,target)]
            # set of n, has a start index from nums list
            # return a list of all n-set that sums up to be the target
            res = []
            # Early termination
            if start >= len(nums) or nums[start] * n > target or nums[-1] * n < target:
                cache[key] = []
                return []
            # base case: find 1 number equal to the target
            if n == 1 and start < len(nums):
                for i in range(start, len(nums)):
                    if nums[i] == target:
                        res.append([nums[i]])
                        break
                cache[key] = res
                return res
            # base case optimization for 2-sum using two pointers
            if n == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append([nums[l], nums[r]])
                        # Skip duplicates for the left pointer.
                        cur_l, cur_r = nums[l], nums[r]
                        while l < r and nums[l] == cur_l:
                            l += 1
                        # Skip duplicates for the right pointer.
                        while l < r and nums[r] == cur_r:
                            r -= 1
                cache[key] = res
                return res
            # recursive case: 
            for i in range(start, len(nums) - n + 1):
                # skip duplicated numbers
                if i > start and nums[i] == nums[i-1]:
                    continue
                # take nums[i] to the final set and append it to all sub sets of n-1 that sums up to target - nums[i]
                subs = n_sum(n-1, i+1, target - nums[i])
                for sub in subs:
                    res.append([nums[i]] + sub)
                cache[key] = res
            return res

        return n_sum(3,0,0)
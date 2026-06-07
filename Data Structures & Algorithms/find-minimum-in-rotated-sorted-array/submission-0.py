class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        ans = hi

        thres = nums[-1]
        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] <= thres:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1


        return nums[ans]
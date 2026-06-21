class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_list = sorted(nums)
        for i in range(k-1):
            sorted_list.pop()
        return max(sorted_list)
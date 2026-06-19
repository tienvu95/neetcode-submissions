class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            # hours to clear all piles at speed k
            return sum((pile + k - 1) // k for pile in piles)

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid        # mid works — but maybe slower still works
            else:
                left = mid + 1     # mid too slow — answer must be faster
        return left

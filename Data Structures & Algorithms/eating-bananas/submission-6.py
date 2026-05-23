from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        ans = max(piles)
        while l <= r:
            mid = (l+r)//2
            n_piles = piles[:]
            hrs = 0
            for n_pile in n_piles:
                hrs += ceil(n_pile/mid)

            if hrs <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
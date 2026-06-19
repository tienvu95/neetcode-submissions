class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)-1):
            stones.sort()
            biggest_stone = stones.pop()
            second_biggest = stones.pop()
            stones.append(biggest_stone-second_biggest)
        return stones.pop()
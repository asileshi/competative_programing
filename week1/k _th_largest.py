class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda y: int(y))
        return nums[-k]
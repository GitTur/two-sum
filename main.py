from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
# num = [2, 7, 11, 15], target = 9

from typing import List


# 브루드 포스트
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in을 이용한 탐색
def twoSum2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# dictionary 사용
def twoSum3(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [nums.index(num), nums_map[target - num]]
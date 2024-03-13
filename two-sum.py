class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = []
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in candidates:
                return [candidates.index(goal), i]
            else:
                candidates.append(nums[i])

# ChatGPT Advice
# Use a dict, which was my original plan, and use enumerate which gives us index and value
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_to_index = {}  # Maps numbers to their indices
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_to_index:
#                 return [num_to_index[complement], i]
#             num_to_index[num] = i

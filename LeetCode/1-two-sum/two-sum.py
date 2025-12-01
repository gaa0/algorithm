class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, v in enumerate(nums):
            comp_num = target - v
            if comp_num in num_dict:
                return [i, num_dict[comp_num]]
            num_dict[v] = i
            
        return []
            
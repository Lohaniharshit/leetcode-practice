class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(0,len(nums),1):
            for j in range((i+1), len(nums),1):
                if nums[i]+nums[j] == target:
                    output.append(i)
                    output.append(j)
                    return output


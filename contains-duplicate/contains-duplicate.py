class Solution1: # time limit exceeded
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False

class Solution2: # accepted: not the fastest
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False

# class Solution3: # not my solution but one of the best:
#     def contains_duplicate(nums: list[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
#
#
# if __name__ == '__main__':
#     import json, sys
#     with open('user.out', 'w') as f:
#         for nums in map(json.loads, sys.stdin):
#             result = contains_duplicate(nums)
#             print(str(result).lower(), file=f)
#     sys.exit()   


class Solution4: # one of the best solution
    def containsDuplicate(self, nums: List[int]) -> bool:

        count = set()

        for n in nums:
            if n in count:
                return True
            
            count.add(n)
        
        return False

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left=0
        for i in range(len(nums)):
            if nums[i] !=val:
                nums[left]=nums[i]
                left+=1
        return left
if __name__ == "__main__":
     nums=[3,2,2,3]
     val=3
     result=Solution().removeElement(nums,val)
     print(nums)



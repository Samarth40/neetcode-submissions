class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        result = []

        for i in range(0,len(arr)):
            if i>0 and arr[i] == arr[i - 1]:
                continue
            left = i + 1
            right = len(arr) - 1
            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]
                if curr_sum == 0:
                    result.append([arr[i],arr[left],arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left -1]:
                        left+=1
                    while left < right and arr[right] == arr[right + 1]:
                        right-=1
                elif curr_sum > 0:
                    right-=1
                else:
                    left+=1
        return result

        
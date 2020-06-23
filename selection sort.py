def sort(nums):
    for i in range(len(nums) - 1):
        minpos = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp



nums = []
n = int(input("enter size"))
for i in range(n):
    nums.append(int(input("enter value")))
sort(nums)
print(nums)

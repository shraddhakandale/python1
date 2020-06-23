def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]





nums = []
n = int(input("enter the size"))
for i in range(n):
    nums.append(int(input("enter value")))

sort(nums)
print(nums)

nums=[4,2,1,0,0,5]
pos=0
for i in nums:
    if i !=0:
        nums[pos]=i
        pos+=1
while pos<len(nums):
    nums[pos]=0
    pos+=1  

print(nums)   
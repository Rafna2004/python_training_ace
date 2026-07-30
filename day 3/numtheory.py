nums=[3,1,3,2,5]
n=len(nums)
exp_sum=n*(n+1)//2
actual_sum=sum(nums)
missing=exp_sum-actual_sum
print("The missing number is:",missing)
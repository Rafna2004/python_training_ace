nums=[3,1,2,3,5]
n=len(nums)
exp_sum=(n*(n+1)/2)
act_sum=sum(nums)
exp_sq_sum = (n * (n + 1) * (2 * n + 1)) / 6
act_sq_sum=sum([i*i for i in nums])
diff_linear=exp_sum-act_sum
diff_sq=exp_sq_sum-act_sq_sum
sum_linear=diff_sq//diff_linear
missing=(sum_linear+diff_linear)//2
duplicate=sum_linear-missing
print(missing)
print(duplicate)
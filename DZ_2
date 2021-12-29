nums = []
sum1 = 0
sum2 = 0
for i in range (1,1001):
    if i % 2 != 0:
        nums.append(i**3)
for idx in range(len(nums)):
    num_sum=0
    j = nums [idx]
    while j:
        num_sum +=  j % 10
        j = j // 10
    if num_sum % 7 == 0:
        sum1 += nums[idx]
    nums[idx] += 17
    num_sum = 0
    j = nums [idx]
    while j:
        num_sum += j % 10
        j = j // 10
    if num_sum % 7 == 0:
        sum2 += nums[idx]
print(sum1)
print(sum2)
nums = list(map(int,input().split()))
target  = int(input("Enter target value: "))
result = []
# for i in range(len(nums)):
#     s = nums[i]
#     for j in range(i+1,len(nums)):
#         s += nums[j]
#         if s == target:
#             result.append(i)
#             result.append(j)
#             return result
#         else:
#             s -= nums[j]
freq = {}
for i in range(len(nums)):
    required = target - nums[i]
    if required in freq:
        result.append(freq[required])
        result.append(i)
        print(result)
    freq[nums[i]] = i
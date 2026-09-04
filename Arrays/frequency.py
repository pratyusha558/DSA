arr = [1,2,2,3,5,5,6,6]
count = {}
for i in range(len(arr)):
  count[arr[i]] = count.get(arr[i],0)+1

print(count)
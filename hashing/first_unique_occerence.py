arr = [2,3,4,1,5,6,2,3,4,5]
seen = {}
for i in range(len(arr)):
    seen[arr[i]] = seen.get(arr[i],0)+1

for key,val in seen.items():
    if val == 1:
        print(key)
        break
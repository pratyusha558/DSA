arr = [1,1,2,3,3,4,4,4]
slow = 0
fast = 1
while fast != len(arr):
  if arr[slow] == arr[fast]:
    fast += 1
  else:
    slow += 1
    arr[slow] = arr[fast]
    fast += 1
print(arr[:slow+1])

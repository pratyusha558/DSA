arr = [0,0,1,2,0,0,3]
slow = 0
for fast in range(0,len(arr)):
  if arr[fast] != 0:
    arr[slow], arr[fast] = arr[fast], arr[slow]
    slow += 1

print(arr)
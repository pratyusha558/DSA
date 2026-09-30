arr = [-1, 0, 1, 2, -1, -4]
arr.sort()
print(arr)
for i in range(len(arr)-2): #because at value i before last two elements it doesnt have two enough elements
  if i > 0 and arr[i] == arr[i-1]:
    continue
  else:
    left = i+1
    right = len(arr) - 1
    total = arr[i] + arr[left] + arr[right]
    while left < right:
      if total == 0:
        print(arr[i],arr[left],arr[right])
        left += 1
        right -= 1
      elif total > 0:
        right -= 1
      else:
        left += 1

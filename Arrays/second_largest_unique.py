arr = [-5, -2, -8, -10]

largest = arr[0]
second = -1
for i  in range(1,len(arr)):
  if arr[i] > largest:
      second = largest
      largest = arr[i]

  elif arr[i] < largest and arr[i] > second:
    second = arr[i]

print(second)
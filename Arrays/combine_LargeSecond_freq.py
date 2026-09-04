arr = [9,9,9]

count1 = 1
count2 = 0
largest  = arr[0]
second = float('-inf')

for i in range(1,len(arr)):
  if arr[i] > largest:
    second = largest
    largest = arr[i]
    count2 = count1
    count1 = 1
  elif arr[i] < largest and arr[i] > second:
    second = arr[i]
    count2 = 1
  elif arr[i] == largest:
    count1 += 1
  elif arr[i] == second:
    count2 += 1


print(largest,count1)
if second == float('-inf'):
    print("No second largest element")
else:
    print(second, count2)
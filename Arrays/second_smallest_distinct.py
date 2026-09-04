arr = [4, 2, 7, 2, 9, 4, 5, 7]
smallest = arr[-1]
second = float('inf')
n = len(arr)
smallest_idx = n - 1
second_idx = -1

for i in range(n-2,-1,-1):
  #checks whether value is less than smallest value
  if arr[i] < smallest:
    second = smallest
    smallest = arr[i]
    second_idx = smallest_idx
    smallest_idx = i

  #if the value is greater than smallest but smaller than the smallest then second smallest will be 
  #value so we replace the second with value and upate with the idx
  elif arr[i] > smallest and arr[i] < second:
    second = arr[i]
    second_idx = i

#displays the second smallest value and index value of last occurence
print("Second smallest value is",second,"with index",second_idx)

arr = [1, 2, 1, 1, 1, 3, 2]
target = 5
left = 0
right = 0
s = 0
max_length = 0
while right < len(arr):
  s += arr[right]
  while s > target:
    s -= arr[left]
    left += 1

  max_length = max(max_length,right-left+1)
  right += 1

print(max_length)
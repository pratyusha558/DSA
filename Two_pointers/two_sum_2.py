# arr = [1, 2, 4, 6, 8, 1, 11]
# target = 10
# left = 0
# right = len(arr) - 1
# while left < right:
#   if arr[left] + arr[right] == target:
#     print(arr[left],arr[right])
#     break
#   elif arr[right] +arr[left] > target:
#     right -= 1
#   else:
#     left += 1
# if left >= right:
#   print("No such pair")

arr = [1, 1, 2, 4, 6, 8, 11]
target = 10

left = 0
right = len(arr) - 1

found = False

while left < right:

    total = arr[left] + arr[right]

    if total == target:
        print(arr[left], arr[right])
        found = True
        break

    elif total > target:
        right -= 1

    else:
        left += 1

if not found:
    print("No such pair")
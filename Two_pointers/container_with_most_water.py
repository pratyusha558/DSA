arr = [1,8,6,2,5,4,8,3,7]

left = 0
right = len(arr) - 1

max_water = 0

while left < right:

    height = min(arr[left], arr[right])
    width = right - left
    area = height * width

    max_water = max(max_water, area)

    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1

print(max_water)
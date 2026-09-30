arr = [2, 3, 1, 2, 4, 3]
target = 7
left = 0
right = 0
s = 0
min_length = 9999999999
while right < len(arr):
    s += arr[right]   #expand until the condition is satisfied
    while s >= target:    #shrink while the condition is satisfied
        min_length = min(min_length,right-left+1)
        s -= arr[left]

        left+=1
    
    right+=1
print(min_length)

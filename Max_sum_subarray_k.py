arr = list(map(int,input("Enter array elements: ").split()))
k = int(input("Enter subarray size: "))

sum_subarray = sum(arr[0:k])
max_sum = sum_subarray

for i in range(k+1,len(arr)):
  sum_subarray += arr[i]-arr[k-i+1]
  max_sum = max(max_sum,sum_subarray)

print(f"Max sum of a subarray in given array is: {max_sum}")
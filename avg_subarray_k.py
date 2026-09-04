arr = list(map(int,input("Enter array elements: ").split()))
k = int(input("Enter subarray size: "))

sum_subarray = sum(arr[0:k])
print(sum_subarray / k)

for i in range(k+1,len(arr)):
  sum_subarray += arr[i]-arr[k-i+1]
  print(sum_subarray / k)


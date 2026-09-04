arr = list(map(int,input("Enter the elements: ").split()))
k = int(input("Enter size of subarray: "))

sub_arr = [] #array to store window values
neg_ele = [] #for storing negative elements
for i in range(0,k):
  sub_arr.append(arr[i])
  if sub_arr[i] < 0:                        #checks the every element
    neg_ele.append(sub_arr[i])
print(neg_ele)

for i in range(k,len(arr)):
  sub_arr.append(arr[i])
  if arr[i] < 0:
    neg_ele.append(arr[i])
  neg = sub_arr.pop(0)
  if neg in neg_ele:
    neg_ele.remove(neg)
  print(neg_ele)
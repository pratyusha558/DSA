
#used for finding the all ocuurences

# arr = [1,2,3,4,2,1,3,2,1,3,2,1]
# k = 3
# idx = []
# for i in range(len(arr)):
#   if arr[i] == k:
#     idx.append(i)

# if not idx:    #checks if there is no index is inserted then idx list is empty 
#   print(-1)
# else:
#   print(idx)



#for finding the first and last occurences

# arr = [1,2,3,4,2,1,3,2,1,3,2,1]
# first = -1
# last = -1
# k = 3

# for i in range(len(arr)):
#   if arr[i] == k:
#     if first == -1:
#       first = i
#     last = i

# print(first,last)


#finding the first occurence of max element


arr = [1,2,4,2,6,8,3]
max_ele = arr[0]
idx = -1

for i in range(len(arr)):
  if arr[i] > max_ele:
    max_ele = arr[i]
    idx = i

print(max_ele,idx)


arr = [5, 2, 3, 4]

# count = 0
# max_element = arr[0]
# for i  in range(1,len(arr)):
#   if arr[i] > max_element and count == 0:
#     max_element = arr[i]
#     count += 1
    
#   elif arr[i] > max_element and count != 0:
#     count = 0
#     max_element = arr[i]
#     count += 1

#   elif arr[i] == max_element:
#     count += 1

  


# print(max_element,count)



count = 1
max_element = arr[0]
for i  in range(1,len(arr)):
  if arr[i] > max_element:
    max_element = arr[i]
    count = 1

  elif arr[i] == max_element:
    count += 1

  


print(max_element,count)
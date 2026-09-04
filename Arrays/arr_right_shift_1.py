# arr = [1,2,3,4,5]
# temp = []                                               only useful for right shif by 1
# temp.append(arr[-1])
# print(temp+arr[:-1])




# arr = [1,2,3,4,5]
# k = 3 #this is performing the only for the this array as the k is 3 the array is len of 5 and easy to take ellemnts by k index but
#not applicable for arr = [1,2,3,4,5,6,7,8] as the code start from index not the last elemnts for this arr        
# temp = arr[k-1:]
# print(temp + arr[:k-1])


#ALGO
#split the arr upto the k elements and add the array to the first splited array half
# arr = [1,2,3,4,5,6,7]
# k = 3   #final approach for right shift by k
# temp = arr[len(arr)-k:]
# print(temp + arr[:len(arr)-k])


# arr = [1,2,3,4,5,6,7]
# k = 3
# temp = []
# for i in range(k,0,-1):
#   temp.append(arr[len(arr)-i])

# arr[:] = arr[:len(arr)-k]
# print(temp+arr)



# arr = [1,2,3,4,5,6,7]
# arr = arr[::-1]
# k = 3
# print(list(reversed(arr[:3]))+ list(reversed(arr[3:])))



#REVERSAL ALGORITHM (sawping the elemnts)
#takes upto O(n) and O(1)


# def reverse(arr,left,right):
#   while left < right:
#     arr[left],arr[right] = arr[right],arr[left]
#     left+=1
#     right-=1

#   return arr
 

# arr = []
# k = 5
# try:
#   k = k%len(arr)
#   reverse(arr,0,len(arr)-1)
#   reverse(arr,0,k-1)
#   reverse(arr,k,len(arr)-1)
#   print(arr)
# except ZeroDivisionError:
#   print("The array has no elements to perform")


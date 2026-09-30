s = "Madam"
s = s.lower()
left = 0
right = len(s) -1
while left < right:
  if s[left] == s[right]:
    left +=1 
    right -=1
  else:
    break

if left == right:
  print("Yes it is a palindrome")
else:
  print("Not a palindrome")
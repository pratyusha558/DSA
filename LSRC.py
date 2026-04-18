s = input("Enter a string like format (abcabcbb) or your wish : ")
char_set = set()
max_Length = 0
left = 0
for i in range(len(s)):
    while s[i] in char_set:
        char_set.remove(s[left])
        left+=1
    char_set.add(s[i])
    max_Length = max(max_Length,i-left+1)
print("Max_length of substring with not repeating charactes is : ",max_Length)
s = input("Enter a string like format (abcabcbb) or your wish : ")
char_set = set()
import time
# max_Length = 0
# left = 0
# for i in range(len(s)):
#     while s[i] in char_set:
#         char_set.remove(s[left])
#         left+=1
#     char_set.add(s[i])
#     max_Length = max(max_Length,i-left+1)
# print("Max_length of substring with not repeating charactes is : ",max_Length)

sub_str = ""
max_len = 0
for i in range(len(s)):
    start = time.time()
    if s[i] in set(sub_str):
        while s[i] in sub_str:
            sub_str = sub_str[1:]
    print(time.time() -start)
    sub_str += s[i]
    max_len = max(max_len,len(sub_str))

print(max_len)

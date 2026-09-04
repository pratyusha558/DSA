s = input("Enter the string: ")
k = int(input("Enter size of substring: "))

sub_str = "" #array to store window values
vowels = "AEIOUaeiou" #for storing negative elements
count = 0 #for number of vowels track
for i in range(0,k):
  sub_str += s[i]
  if sub_str[i] in vowels:                        #checks the every element
    count += 1
max_len = count

for i in range(k,len(s)):
  sub_str += s[i]
  if s[i] in vowels:
    count += 1
  fst = sub_str[0]          #gets the first element
  sub_str = sub_str[1:]
  if fst in vowels:          #checks if first element is in vowels if there then decreases the vowel count as we remove the first element in sub string
    count -= 1
  max_len = max(max_len,count)
print(max_len)
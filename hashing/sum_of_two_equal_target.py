arr = [2, 7, 11, 15]
target = 9
seen = set()
flag = False
for i in arr:
  if target - i in seen:      #checks whether target - i that me element to sum up to get target is present in set 
    flag = True
  else:
    seen.add(i)
if flag:
  print("YEs")
else:
  print("NO")

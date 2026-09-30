
"""Its simple logic for contains duplicate"""
# arr = [4, 2, 7, 2, 9, 5]
# if len(arr) == len(set(arr)):
#   print("NO")
# else:
#   print("YES")

"""Now using hashing"""
arr = [4, 2, 7, 4, 9, 5]
seen = {}
for i in range(len(arr)):
  if arr[i] in seen.values():
    print(f"Yes duplicates present - {arr[i]}")
  else:
    seen[i] = arr[i]

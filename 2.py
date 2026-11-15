#  Find the Largest Element in Each Row
# Find the largest element from each row without using max().
# numbers = [
#  [12, 45, 23],
#  [67, 34, 89],
#  [21, 90, 56]
# ]
# Expected output:
# 45
# 89
# 90

numbers = [
  [12, 45, 23],
  [67, 34, 89],
  [21, 90, 56]
 ]

for i in numbers:
    print(max(i))


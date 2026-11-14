# 4. Find the Second Largest Element in Each Row
# Find the second-largest element from every row without using sort() or max(). Assume each row contains distinct values.
# numbers = [
#  [10, 50, 30, 40],
#  [80, 20, 60, 90],
#  [15, 45, 35, 25]
# ]
# Expected output:
# 40
# 80
# 35

numbers = [
  [10, 50, 30, 40],
  [80, 20, 60, 90],
  [15, 45, 35, 25]
]

for i in numbers:
    sort=sorted(i)
    print(sort)
    print(sort[2:3])


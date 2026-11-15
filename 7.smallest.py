# Find the smallest number in each row without using the min() function.
# Sample Input:
# numbers = [
#  [12, 5, 18, 9],
#  [45, 23, 67, 10],
#  [8, 14, 3, 20]
# ]

numbers = [
  [12, 5, 18, 9],
  [45, 23, 67, 10],
  [8, 14, 3, 20]
]

for i in numbers:
    sort=sorted(i)
    
    print("smallest:",sort[:1])
# Find Common Elements Between Two Nested Lists
# Treat all inner lists as one collection of values. Find the elements present in both nested lists and display them without
# duplicates.
# list1 = [[10, 20, 30],
#  [40, 50, 60]
# ]
# list2 = [
#  [30, 40, 70],
#  [80, 10, 90]
# ]
# Expected output:
# [10, 30, 40]

list1 = [[10, 20, 30],
  [40, 50, 60]
 ]

list2 = [
  [30, 40, 70],
  [80, 10, 90]
 ]

new=[]
new2=[]
for i in list1:
    for j in i:
        new.append(j)

for i in list2:
    for j in i:
        new2.append(j)

common=[]
for i in new:
 if i in new2:
    common.append(i)

print(common)
    
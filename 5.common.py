# 5. Find Common Elements Between Two Nested Lists
# Treat all inner lists as one collection of values. Find the elements present in both nested lists and display them without
# duplicates.

# list1 = [ [10, 20, 30],
#  [40, 50, 60]
# ]
# list2 = [
#  [30, 40, 70],
#  [80, 10, 90]
# ]

list1 = [ [10, 20, 30],
  [40, 50, 60]
 ]

list2 = [
  [30, 40, 70],
  [80, 10, 90]
 ]

new_list1=[]
new_list2=[]

for i in list1:
    for j in i:
        new_list1.append(j)

for i in list2:
    for j in i:
        new_list2.append(j)


print([i for i in new_list1 if i in new_list2])
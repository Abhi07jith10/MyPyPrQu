# Transpose a Matrix
# Convert the given nested list into its transpose.
# numbers = [
#  [10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]
# ]
# Expected output:
# 10 40 70
# 20 50 80
# 30 60 90

numbers = [
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]
 ]

new=[]
for i in numbers:
    for j in i:
        new.append(j)

print(new[0],new[3],new[6])
print(new[1],new[4],new[7])
print(new[2],new[5],new[8])

# Row-wise and Column-wise Sum
# Calculate the total marks of each student and the total marks of each subject.
# marks = [
#  [80, 75, 90],
#  [65, 85, 70],
#  [90, 95, 85]
# ]
# Expected output:
# Student totals: 245, 220, 270
# Subject totals: 235, 255, 245

marks = [
  [80, 75, 90],
  [65, 85, 70],
  [90, 95, 85]
 ]

print(f"row wise total: {sum(marks[0]),sum(marks[1]),sum(marks[2])}")


C1=marks[0][0]+marks[1][0]+marks[2][0]
C2=marks[0][1]+marks[1][1]+marks[2][1]
C3=marks[0][2]+marks[1][2]+marks[2][2]
print(f"coloumn wise total: {C1,C2,C3}")

num = [4, 2, 6, 8, 10]

smallest = num[0]
second_smallest = num[1]

for i in num:
    if i < smallest:
        second_smallest = smallest
        smallest = i

    elif i < second_smallest and i != smallest:
        second_smallest = i

print("Second smallest:", second_smallest)

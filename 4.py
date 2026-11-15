from functools import reduce

nums = [4, 9, 2, 7]

print(reduce(lambda a, b: a if a > b else b, nums))
 # nums=[1,2,3,4,5]

 # print(list(map(lambda a:a**2,nums)))

# nums=[2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda a:a%2==0,nums)))

nums=[1,2,3,4,5,6]

from functools import reduce
print((reduce(lambda a,b:a+b,nums)))

1
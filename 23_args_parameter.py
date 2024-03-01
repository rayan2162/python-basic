# args = parameter that will pack all arguments into a tuples

def add(*nums):
    sum = 0
    for i in nums:
        sum = sum + i
    print(sum)

add(1,2,3,4,5,6,7,8,9,10)


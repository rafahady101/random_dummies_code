''' Generator '''

print(10*"=","EX 1","="*10)
def square(n):
    square_list = []
    for index in range(n):
        square_list.append(index**2)
    return square_list

print(square(10))
print()



print(10*"=","EX 2","="*10)
def random(low,high,n):
    
    for x in range(n):
        import random
        x = random.randint(low,high)
        yield x

for num in random(1,10,12):
    print(num)
print()



print(10*"=","EX 3","="*10)
s = "hello"
s_iteration = iter(s)
print(next(s_iteration))
print(next(s_iteration))
print(next(s_iteration))
print(next(s_iteration))
print(next(s_iteration))



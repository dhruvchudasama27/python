# print this :- 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ... 10000
number = 0
ans = 1
print(number,end=' ')
while number < 9870:
    number = number + ans 
    print(number,end=' ')
    ans = ans + 1 

# number = number + ans #number = 3
# print(number)
# ans = ans + 1 #ans = 3
# number = number + ans # number = 6
# print(number)

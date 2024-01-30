# Write a programe to print following pattern 
# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 .... 3000 
number = 2
ans = 1
print(number,end=' ')
print(ans,end=' ')

while number < 1364:
    number = number + ans
    print(number,end=' ')
    ans = number + ans
    print(ans,end=' ')
# number = number + ans
# print(number)
# ans = number + ans
# print(ans)




# Write a programe to findout product execpt self from list 
# number = [1,2,4,5,10]
# answer = [400,200,100]

def getExceptSelf(number,c):
    answer = []
    flash = 0
    for i in range(1,c+1):
        b = int(input("Enter any number:- "))
        a.append(b)
    while flash < len(number):
        temp = 1 
        count = 0
        while count < len(number):
            temp = temp * number[count] 
            count+=1
        answer.append(int(temp / number[flash]))
        flash+=1
    return answer

c = int(input("How many you have insert a number :-"))
a = []
num = getExceptSelf(a,c)
print("Your wishlist numbers ",a)
print("answer is ",num)



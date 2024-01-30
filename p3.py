# Write a programe to count total number of odd and even numbers in the given list 
numbers = [205,201,15,12,495,7654]
odd_number = []
even_number = []
counter = {'odd_numbers' : 0, 'even_numbers' : 0}
count = 0
while count < len(numbers):
    if numbers[count] % 2 == 0:
        print("number is even")
        even_number.append(numbers[count])
        if even_number in numbers:
            counter['even_numbers']=+1

    else:
        print("number is odd")
        odd_number.append(numbers[count])
        if odd_number in numbers:
            counter['odd_numbers']=+1
    count+=1
print("Even numbers is:- ",even_number)
print("Odd numbers is:- ",odd_number)
print(counter)
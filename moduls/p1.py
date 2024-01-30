# Write a programe to create roulete game 
import random

game = [10,7,15,45,76,12,36,53]
user = int(input("Enter any two digit of number:-"))
select = random.choice(game)
print(select)

if user == select:
    print("you are winner")
else:
    print("Batter luck next time")
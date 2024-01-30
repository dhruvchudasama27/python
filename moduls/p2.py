import random

qustions = [ {'Which animal is known as the Ship of the Desert?':'camel'} , {'How many days are there in a week?':'7'} , {'How many letters are there in the English alphabet?':'26'} , {'Which animal is known as the king of the jungle?':'lion'} , {'what is the 5*5 ':'25'} ]
random.shuffle(qustions)
key =[]
value =[]
# count = 0
score = 0

for i in qustions:
    key.append(list(i.keys()))
    value.append(list(i.values()))
    print(key[count])
    print(value[count])
    count+=1
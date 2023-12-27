# Implement a simple text-based Rock-Paper-Scissors game. 
# Prompt the user to choose rock, paper, or scissors, and then randomly generate the computer's choice. 
# Determine the winner based on the game rules.

game = { "rock" , "paper" , "scissors"}
user = input("Enter rock or paper or scissors : ")

if user == "rock":
    print("you select :- rock")
    print("computer select :-",list(game)[0])
    if list(game)[0] == "rock":
        print("match tie")
    elif list(game)[0] == "paper":
        print("computer is winner")
    elif list(game)[0] == "scissors":
        print("you are winner")
elif user == "paper":
    print("you select :- paper")
    print("computer select :-",list(game)[0])
    if list(game)[0] == "rock":
        print("you are winner")
    elif list(game)[0] == "paper":
        print("match tie")
    elif list(game)[0] == "scissors":
        print("computer is winner")
elif user == "scissors":
    print("you select :- scissors")
    print("computer select :-",list(game)[0])
    if list(game)[0] == "rock":
        print("computer is winner")
    elif list(game)[0] == "paper":
        print("you are winner")
    elif list(game)[0] == "scissors":
        print("match tie")
else :
    print("take write input")

# print(list(game)[0])

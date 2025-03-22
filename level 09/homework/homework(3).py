print("you have to enter rock,paper or scissors")
p1 = input("enter your choise: ")
p2 = input("enter your choise: ")
def rps(p1, p2):
    if p1==p2:
        return 'Draw!'
    elif p1=="scissors" and p2=="paper":
        return "Player 1 won!"
    elif p1=="rock" and p2=="scissors":
        return "Player 1 won!"
    elif p1=="paper" and p2=="rock":
        return "Player 1 won!"
    else:
        return"Player 2 won!" 
print(rps(p1,p2))
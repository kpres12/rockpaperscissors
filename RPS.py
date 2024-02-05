import random
print("Welcome to Rock Paper Scissors")

playing = input("Do you want to play?")

if playing != "yes":
	print ("Goodbye bitch")
	quit()
print("Swaggy p, lets play")

options = ["rock", "paper", "scissors"]

player = input("rock, paper, or scissors?")
computer = random.choice(options)
print("You chose " + player)
print("Computer chose " + computer)
if player == computer:
	print("It's a tie")
elif player == "rock" and computer == "scissors":
	print("You win")
	

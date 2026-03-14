import random
choices=["rock","paper","scissors"]
user=input("Enter rock or paper or scissors:").lower()
computer=random.choice(choices)
print("Computer chooses:",computer)
if user==computer:
  print("It's a tie")
elif (user=="rock" and computer=="scissors") or \
     (user=="scissors" and computer=="paper") or \
     (user=="paper" and computer=="rock"):
  print("You win!")
elif user in choices:
  print("Computer wins!")
else:
  print("Invalid choice")

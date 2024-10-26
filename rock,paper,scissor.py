import random
def get_choices():
    player_choice= input("enter a choice(rock , paper, scissors)      ")
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options)
    choices ={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player , computer):
  print(f"you chose {player}, computer chose {computer}")

  if player == computer:
     return "it's a tie"
  elif player == "rock":
    if computer == "scissor":
     return "rock smashes scissors! you win!"
    else:
     return "paper covers rock! you lose."
  elif player == "paper":
    if computer == "rock":
     return "paper covers rock! you win!"
    else:
     return "scissors cut paper! you lose."
  elif player == "scissor":
    if computer == "paper":
     return "scissor cut paper! you win!"
    else:
     return "rock smashes scissor! you lose." 

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

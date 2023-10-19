import art
from game_data import data
import random
from replit import clear

def get_random_instagram_account(list):
  """Get data from random account"""
  return random.choice(list)

def get_data_formated(dictionary):
  """Format account into a printable forma: Name, description and country from"""
  name = dictionary["name"]
  description = dictionary["description"]
  country = dictionary["country"]
  return f"{name}, a {description} from {country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(art.logo)
  score = 0
  game_should_continue = True
  a_account = get_random_instagram_account(data)
  b_account = get_random_instagram_account(data)
  
  while game_should_continue:
    a_account = b_account
    b_account = get_random_instagram_account(data)

    while a_account == b_account:
      b_account = get_random_instagram_account(data)

    print(f"Compare A: {get_data_formated(a_account)}.")
    print(art.vs)
    print(f"Compare B: {get_data_formated(b_account)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_followers_count = a_account["follower_count"]
    b_followers_count = b_account["follower_count"]
    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    clear()
    print(art.logo)

    if is_correct:
      score += 1
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")


game()

#Display art
#get random account a and b from dictionary
# Format the account data into a printable format
#Ask user for a guess
#Check the answer - if is correct.
## Get follower count of each account.
## The if statement to check if user is correct.
#Give user feedback on their guess.
#Make the game repeatable.
#Make account at position B become the next account at position A 
#Clear the screen between rounds.
import art
import game_data
import random
import replit

def get_next_accounts(a = {}, b = {}):
  if a and b:
    a = b  
  else:
    a = random.choice(game_data.data)

  b = random.choice(game_data.data)

  while a == b:
    b = random.choice(game_data.data)
    
  return a, b
  
def main():
  next_game = True
  score = 0

  a = {}
  b = {}

  while next_game:
    replit.clear()
    print(art.logo)

    a, b = get_next_accounts(a, b)

    if score > 0:
      print(f"You're right! Current score: {score}.")  

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice == 'A' and a['follower_count'] > b['follower_count']:
      score += 1
    elif choice == 'B' and b['follower_count'] > a['follower_count']:
      score += 1
    else:
      next_game = False

  replit.clear()
  print(art.logo)
  print(f"Sorry, that's wrong. Final score: {score}")


main()
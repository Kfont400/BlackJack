import random
from os import system, name
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

#Start game
def black_jack():
  print(hit_me(my_hand()))
  

#hit computer for extra cards
def hit_dealer(dealer_hand):
  soft_num = cards[0]
  dealer_choice = ['y', 'n']
  decision = str(random.choice(dealer_choice))
  keep_going = True
  while keep_going:
    
    dealer_hand_total = sum(dealer_hand)
    dealer_hand, dealer_hand_total = switch_ace_value(hand = dealer_hand , hand_total= dealer_hand_total)
    if dealer_hand_total < 22:
      if dealer_hand_total == 21 and len(dealer_hand) == 2:
        keep_going = False
      elif dealer_hand_total == 21:
        keep_going = False
      elif dealer_hand_total < 17:
        dealer_hand.append(pull_deck(dealer_hand_total))
      elif soft_num in dealer_hand and 16 >= dealer_hand_total != 21:
        dealer_hand.append(pull_deck(dealer_hand_total))
        keep_going = True
      elif dealer_hand_total <= 10:
        dealer_hand.append(pull_deck(dealer_hand_total))
      elif decision == 'y':
        dealer_hand.append(pull_deck(dealer_hand_total))
        keep_going = True
      else:
        keep_going = False
    else:
      keep_going = False
  return dealer_hand
#hit me for extra cards
def hit_me(my_hand):
  dealer_initial_hand = hit_dealer(dealer_hand())
  keep_going = True
  while keep_going:
    
    my_hand_total = sum(my_hand)
    my_hand, my_hand_total = switch_ace_value(my_hand, my_hand_total)
   
    if my_hand_total < 22:
      print(f"Your Hand: {my_hand} = {my_hand_total} \nDealer hand: {[dealer_initial_hand[0]]}")
      new_card = input("What would you like another card? ").lower()
      if new_card == 'y':
        my_hand.append(pull_deck(my_hand_total))
        keep_going = True
      elif new_card == 'n':
        keep_going = False
      else:
        print(f'Invalid entry')
        continue
    else:
      keep_going = False
  
  return game_over(my_hand, my_hand_total, dealer_initial_hand)

def switch_ace_value(hand, hand_total):
  if hand_total >= 22 and hand_total != 21 and 11 in hand:
      index = hand.index(11)
      hand[index] = 1 
      hand_total = sum(hand)
  return hand, hand_total
#is the game over
def game_over(my_hand ,my_hand_total, dealer_final_hand):
  dealer_final_total = sum(dealer_final_hand)
  bust = 22
  blackjack = 21
  winner = 'You win!'
  loser = 'You lose!'
  tie = 'No winner'

  if my_hand_total == blackjack and len(my_hand) == 2:
    return f"{my_hand} = {my_hand_total} \nDealer hand: {dealer_final_hand} = {dealer_final_total}\n{winner} with Blackjack!"
  elif dealer_final_total == blackjack and  my_hand_total != blackjack:
    return f"{my_hand} = {my_hand_total} \nDealer hand: {dealer_final_hand} = {dealer_final_total}\n{loser} Dealer has Blackjack!"
  elif dealer_final_total == 21 and  my_hand_total != blackjack:
    return f"{my_hand} = {my_hand_total} \nDealer hand: {dealer_final_hand} = {dealer_final_total}\n{loser} Dealer has win!"
  elif my_hand_total >= bust:
    return f"{my_hand} = {my_hand_total} \nBusted {loser}"
  elif dealer_final_total >= bust:
    return f"{my_hand} = {my_hand_total} \nDealer hand: {dealer_final_hand} = {dealer_final_total}\n{winner}"
  else:
    if my_hand_total == dealer_final_total:
      return f"{my_hand} = {my_hand_total} \nDealer hand: {dealer_final_hand} = {dealer_final_total}\n{tie}"
    elif my_hand_total > dealer_final_total:
      return f"{my_hand} = {my_hand_total} \nDealer hand: {dealer_final_hand} = {dealer_final_total}\n{winner}"
    elif my_hand_total < dealer_final_total:
      return f"{my_hand} = {my_hand_total} \nDealer hand: {dealer_final_hand} = {dealer_final_total}\n{loser}"
    

#Pull card to deck
def pull_deck(card_total):
  rand_card = random.choice(cards)
  if card_total > 21 and rand_card == 11:
    return 1
  return rand_card

#my initial hand
def my_hand():
  my_hand = []
  my_hand_total = sum(my_hand) 
  while len(my_hand) < 2:
    my_hand.append(pull_deck(my_hand_total))
  return my_hand
    
#dealer's initial hand
def dealer_hand():
  dealer_hand = []
  dealer_hand_total = sum(dealer_hand)  
  while len(dealer_hand) < 2:
    dealer_hand.append(pull_deck(dealer_hand_total))
  return dealer_hand


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


#start game
new_game = True
while new_game:
  print(logo)
  black_jack()
  if input("Play again? Type 'y' to  continue, type 'n' to stop: ").lower() == "y":
    new_game = True
    clear()
  else:
    new_game = False
print("Thanks for playing! ")

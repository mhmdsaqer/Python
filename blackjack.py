import random

from replit import clear
 
def play_game():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  is_over = False
  user_cards=[]
  computer_cards=[]
  
  def compare(user_score, computer_score):
    if user_score == computer_score:
      return "Draw"
    elif user_score == 0:
      return "User won"
    elif computer_score == 0:
      return "Computer won"
    elif user_score > 21:
      return "User score is over , User lost"
    elif computer_score > 21:
      return "Computer score is over , Computer lost"
    elif user_score > computer_score:
      return "user won !!!!!"
    elif computer_score > user_score:
      return "Computer won !!!"
      
      
  
  def deal_card():
    card = random.choice(cards)
    return card
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_over:
      def calculate_cards(cards):
        if sum(cards)==21 and len(cards)==2:
          return 0
      
        if 11 in cards and sum(cards)> 21:
          cards.remove(11)
          cards.append(1)
        
        return sum(cards)
      
      user_score = calculate_cards(user_cards)
      computer_score = calculate_cards(computer_cards)
      
      print(f"your cards is {user_cards} and your score is {user_score}")
      print(f"computer first card is {computer_cards[0]} ")
      
      
      if user_score == 0 or computer_score ==0 or user_score > 21:
        is_over = True
      else:
        want_another_card = input("want another card 'y' or 'n'")
        if want_another_card == 'y':
          user_cards.append(deal_card())
        else:
          is_over= True
    
  while computer_score != 0 and computer_score <17:
      computer_cards.append(deal_card())
      computer_score= calculate_cards(computer_cards)
    
  print(f"your cards are {user_cards} and your score is {user_score}")
  print(f"computer cards are {computer_cards} and its score is {computer_score}")
    
  print(compare(user_score,computer_score))
  
while input("want to play again 'y'or 'n' ?")== 'y':
  clear()
  play_game()


import random
suit_tuple=('Diamond','Club','Heart','Spades')
face_tuple=('ACE','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
deck=[]
for suit in suit_tuple:
    for value, faces in enumerate(face_tuple):
        card={'Face':faces, 'suit':suit, 'value':value+1}
        deck.append(card)

def getcard(deck):
    random.shuffle(deck)
    lastcard=deck.pop()
    
    return lastcard

chances=8
print("Let's play a prediction game related to a deck cards, game name is 'Higher or lower' ")
print("On every right answer you will get 20 points ")
print("On every wrong answer you will be deducted by 15 points ")
print("Let's start ")
score=50

while True:
    current_card=getcard(deck)
    for cards in range(chances):
        card_face=current_card['Face']
        card_suit=current_card['suit']
        card_value=current_card['value']
        print(f"starting card is {card_face} of {card_suit}")
        ans=input("""Will next card be higher or lower, 
                 (h/l) : """)
        new_card=getcard(deck)
        new_face=new_card['Face']
        new_suit=new_card['suit']
        new_value=new_card['value']
        print(f"New card is {new_face} of {new_suit}")
        if ans=='h':
            if new_value>card_value:
                print("Correct prediction")
                score=score+20
                print("Your score is",score)
            else:
                print("Wrong prediction")
                score=score-15
                print("Your score is",score)
                
        elif ans=='l':
            if new_value<card_value:
                print("Correctt prediction")
                score=score+20
                print("Your score is",score)
            else:
                print("Wrong prediction")
                score=score-15
                print("Your score is",score)
        else:
            pass
        current_card=new_card
        
    qut=input("""Do you want to continue, press 'Enter'
              To quit, press 'q'
              : """)
    if qut=='q':
        print("You have quit, Bye!!")
        break
    
    
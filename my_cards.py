import random
face_card = ['2','3','4','5','6','7','8','9','10','Ace','King',"Queen","Jack"]
type_card = ["Hearts", "Diamonds", "Clubs", "Spades"]

deck = set()
def create_deck():
    deck.add(('Joker'))
    for t in type_card:
        for c in  face_card:
            deck.add((c,' of ',t ))
create_deck()
pick_card =random.choice(list(deck))


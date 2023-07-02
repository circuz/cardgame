# Testing different strategies for the card game 31

import random
from cardgame_setup import Game, Deck, Card, SUITS

def shuffle(deck, hand_size = 52, bunch_span = (0,2)):
    # the part of the deck not being shuffled, flipped around
    if hand_size == 0:
        return

    newdeck = deck.cards[:-hand_size]
    newdeck = newdeck[::-1]
    
    hand = deck.cards[-hand_size:]
    hand = hand[::-1]
    while len(hand) > bunch_span[1]:
        bunch = []
        for _ in range(random.randint(bunch_span[0],bunch_span[1])):
            bunch.append(hand.pop())
        newdeck += bunch[::-1]
    newdeck += hand
    
    deck.set_cards(newdeck[::-1])
    return 

def grade_shuffle_naive(deck):
    grade = 0
    for i, card in enumerate(deck.cards):
        grade += abs(1 + i - card.id)
    print(grade)
    return grade

    

deck1 = Deck()
deck2 = Deck()

deck1.show_ids()
shuffle(deck1, hand_size = 52, bunch_span = [1,1])
shuffle(deck2, hand_size = 0, bunch_span = [2,2])
deck1.show_ids()
grade_shuffle_naive(deck1)
deck2.show_ids()
grade_shuffle_naive(deck2)


    

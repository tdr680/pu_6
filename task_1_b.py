#----------------------------------------------------------------------------------------
# task_1_b.py
#----------------------------------------------------------------------------------------

from task_1_a import Card
from random import shuffle


class Deck(object):

    def __init__(self, card_list):
        self.card_list = card_list

    def shuffle(self):
        shuffle(self.card_list)

    def pop_card(self):
        return self.card_list.pop()


#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    deck = Deck(Card.create_deck())  # creates a deck with the given cards
    deck.shuffle()                   # randomizes the order
    deck.pop_card()                  # returns the top card

    # sample game
    cards = Card.create_deck()

    deck = Deck(cards)
    deck.shuffle()

    card1 = deck.pop_card()
    card2 = deck.pop_card()

    if card1 > card2:
        print "Player 1 wins"
    elif card2 > card1:
        print "Player 2 wins"
    else:
        print "It's a tie"
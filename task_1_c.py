#----------------------------------------------------------------------------------------
# task_1_c.py
#----------------------------------------------------------------------------------------

from task_1_a import Card
from task_1_b import Deck


class BlackjackCard(Card):

    def rank_value(self):
        if self.rank == "Ace":
            return 11
        elif self.rank == "2":
            return 2
        elif self.rank == "3":
            return 3
        elif self.rank == "4":
            return 4
        elif self.rank == "5":
            return 5
        elif self.rank == "6":
            return 6
        elif self.rank == "7":
            return 7
        elif self.rank == "8":
            return 8
        elif self.rank == "9":
            return 9
        elif self.rank == "10":
            return 10
        elif self.rank == "Jack":
            return 10
        elif self.rank == "Queen":
            return 10
        elif self.rank == "King":
            return 10

    def __cmp__(self, other):
        return cmp(self.rank_value(), other.rank_value())

#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    cards = BlackjackCard.create_deck()
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

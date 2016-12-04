#----------------------------------------------------------------------------------------
# task_1_a.py
#----------------------------------------------------------------------------------------


class Card(object):

    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, rank):
        """
        :param suit: integer from 0 to 3
        :param rank: integer from 0 to 12
        """
        self.__suit = suit
        self.__rank = rank

    @property
    def suit(self):
        return Card.SUITS[self.__suit]

    @property
    def rank(self):
        return Card.RANKS[self.__rank]

    def __str__(self):
        return "{0} of {1}".format(self.rank, self.suit)

    def __cmp__(self, other):
        return cmp((self.__suit, self.__rank), (other.__suit, other.__rank))

    @classmethod
    def create_deck(cls):
        deck = []
        for s in range(0, len(cls.SUITS)):
            for r in range(0, len(cls.RANKS)):
                deck.append(cls(s, r))
        return deck


#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    # refers to SUITS[0] == "Clubs" and RANKS[0] == "Ace"
    card1 = Card(0, 0)

    # refers to SUITS[1] == "Diamonds" and RANKS[0] == "Ace"
    card2 = Card(1, 0)

    print card1.suit     # "Clubs"
    print card1.rank     # "Ace"

    print card1          # Ace of Clubs
    print card2          # Ace of Diamonds

    print card1 < card2  # True

    # creates a list containing all cards by iterating over RANKS and SUITS
    # the list contains: [Card(0, 0), Card(0, 1), Card(0, 2),...Card(12, 3)]
    deck = Card.create_deck()

    for card in deck:
        print card  # prints 'Ace of Clubs', '2 of Clubs', and so on

    aos = Card(3, 0)
    print aos            # https://www.youtube.com/watch?v=1iwC2QljLn4

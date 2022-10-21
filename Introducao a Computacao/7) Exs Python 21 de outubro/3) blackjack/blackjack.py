from random import randint


class Card:
    sp_cards_dictionary = {
        "king": 10,
        "jack": 10,
        "queen": 10,
        "ace": 1
    }

    def __init__(self, value):
        self.isSpCard = False
        self.isAce = False
        self.name = value
        if type(value) is int and 2 <= value <= 10:
            self.numericValue = value
        elif type(value) is str and value in Card.sp_cards_dictionary:
            self.numericValue = Card.sp_cards_dictionary[value]
            self.isSpCard = True
            self.isAce = True if value == "ace" else False
        else:
            raise Exception("Invalid card value was insert")


class Actor:
    def __init__(self):
        self.cards: list[Card] = []
        self.totAces: int = 0
        self.totAmount: int = 0

    def add_cards(self, card1, card2):
        if card1.isAce:
            self.totAces += 1
        if card2.isAce:
            self.totAces += 1
        self.cards.append(card1)
        self.cards.append(card2)
        self._update_totAmout()

    def _update_totAmout(self):
        self.totAmount = 0  # sets the total amount to 0 and recalculates it
        has_already_found_an_sp_but_not_ace_card = False
        for i in range(0, len(self.cards)):
            self.totAmount += self.cards[i].numericValue  # adds up the value of each car to the value amount
            if self.cards[i].isSpCard and (not self.cards[i].isAce) and (not has_already_found_an_sp_but_not_ace_card):
                has_already_found_an_sp_but_not_ace_card = True
                self.totAmount += self.totAces * 10  # (ace bonus when combine with another sp) - (ace default value)


# Game Loop
flag = True
while flag:

    cards_suit_1 = [Card(2), Card(3), Card(4), Card(5), Card(6), Card(7), Card(8), Card(9), Card(10),
                    Card("king"), Card("queen"), Card("jack"), Card("ace")]
    cards_suit_2, cards_suit_3, cards_suit_4 = cards_suit_1.copy(), cards_suit_1.copy(), cards_suit_1.copy()
    suits = [cards_suit_1, cards_suit_2, cards_suit_3, cards_suit_4]
    # prints the available cards
    for i in range(0, len(suits)):
        print(f"Suit {i}: [", end=" ")
        for card in suits[i]:
            print(card.name, end=" ")
        print("]")


    player: Actor = Actor()
    dealer: Actor = Actor()

    # selects a random suit among the 4, selects a random card, remove the random card from the suit pool
    suit_player = suits[randint(0, 3)]
    player_card1 = suit_player[randint(0, len(suit_player))]
    suit_player.remove(player_card1)
    player_card2 = suit_player[randint(0, len(suit_player))]
    suit_player.remove(player_card2)

    suit_dealer = suits[randint(0, 3)]
    dealer_card1 = suit_player[randint(0, len(suit_player))]
    suit_dealer.remove(dealer_card1)
    dealer_card2 = suit_player[randint(0, len(suit_player))]
    suit_dealer.remove(dealer_card2)

    print()
    # prints the available cards
    for i in range(0, len(suits)):
        print(f"Suit {i}: [", end=" ")
        for card in suits[i]:
            print(card.name, end=" ")
        print("]")

    print()
    print(f"player card: {player_card1.name}")
    print(f"player card: {player_card2.name}")
    print(f"dealer card: {dealer_card2.name}")
    print(f"dealer card: {dealer_card2.name}")
    print()



    while True:
        code = input("wanna play another round? [y/n]: ")
        if code.upper() == "N" or code.upper() == "NO":
            flag = False
            break
        elif code.upper() == "Y" or code.upper() == "YES":
            print("starting another round \n")
            break
        else:
            print("please insert y or n")

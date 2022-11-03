import random


class Card:
    def __init__(self, symbol: str, value: int, suit: str):
        self.symbol = symbol
        self.value = value
        self.suit = suit

    def to_string(self):
        return f"[{self.symbol}{self.suit}]"


class Deck:

    TOT_CARDS_PER_LINE = 14

    def __init__(self, name: str, cards_list: list[Card]):
        self.cards_list = cards_list
        self.name = name

    def to_string(self) -> str:
        string = f"{self.name}: \n"
        counter = 0
        for card in self.cards_list:
            if counter >= Deck.TOT_CARDS_PER_LINE-1:
                string += "\n"
                counter = 0
            string += card.to_string() + " "
            counter += 1
        return string

    def shuffle_it(self) -> None:
        random.shuffle(self.cards_list)

    def _get_last_2_cards(self) -> list[Card]:
        return [self.cards_list[len(self.cards_list)-2], self.cards_list[len(self.cards_list)-1]]

    def get_last_2_cards_as_string(self):
        txt = f"{self.name} last 2 cards: "
        for ending_card in self._get_last_2_cards():
            txt += ending_card.to_string() + " "
        txt += f"| sum = {self.get_sum_of_last_2_cards()}"
        return txt

    def get_sum_of_last_2_cards(self) -> int:
        return self.get_sum_of_last_2_cards()[0].value + self.get_last_2_cards_as_string()[1].value


class Game:

    LIST_OF_SUITS = ["#", "&", "@", "?"]

    def __init__(self):
        self.buying_deck: Deck = Game._get_a_full_deck()
        print(self.buying_deck.to_string()+ "\n")
        self.buying_deck.shuffle_it()

        print(self.buying_deck.to_string()+ "\n")
        self.player_deck: Deck = Deck("player", self.get_14_random_cards_from_buying_deck())
        print(self.player_deck.to_string())
        #self.computer_deck = computer_deck

    @staticmethod
    def _get_a_full_deck() -> Deck:
        buying_cards_list = []
        for k in range(0, len(Game.LIST_OF_SUITS)):
            for i in range(2, 10 + 1):
                buying_cards_list.append(Card(str(i), i, Game.LIST_OF_SUITS[k]))
            buying_cards_list.append(Card("J", 11, Game.LIST_OF_SUITS[k]))
            buying_cards_list.append(Card("Q", 12, Game.LIST_OF_SUITS[k]))
            buying_cards_list.append(Card("K", 13, Game.LIST_OF_SUITS[k]))
            buying_cards_list.append(Card("A", 14, Game.LIST_OF_SUITS[k]))
        return Deck("Buying Deck", buying_cards_list)

    def get_14_random_cards_from_buying_deck(self) -> list[Card]:
        cards = []
        for i in range(0, 14):
            cards.append(self.buying_deck.cards_list[random.randint(0, len(self.buying_deck.cards_list)-1)])
        return cards




Game()


"""
list_of_cards = []
deck1 = Deck("My Deck", list_of_cards)
deck2 = Deck("Computer", list_of_cards.copy())

print("\nINITIAL DECKS ")
print(deck1.to_string())
print(deck2.to_string() + "\n")

deck1.shuffle_it()
deck2.shuffle_it()
print("\nSHUFFLE DECKS ")
print(deck1.to_string())
print(deck2.to_string() + "\n")

print("\nLAST 2 CARDS OF EACH DECK ")
print(deck1.get_last_2_cards_as_string())
print(deck2.get_last_2_cards_as_string() + "\n")

if deck1.get_sum_of_last_2_cards() > deck2.get_sum_of_last_2_cards():
    print(f"{deck1.name} wins")
elif deck1.get_sum_of_last_2_cards() < deck2.get_sum_of_last_2_cards():
    print(f"{deck2.name} wins")
else:
    print("it's a draw")

"""

import random

class Card:
    def __init__(self, symbol: str, value: int):
        self.symbol = symbol
        self.value = value

    def to_string(self):
        return f"[{self.symbol}]"

class Deck:
    def __init__(self, name:str, cards_list: list[Card]):
        self.cards_list = cards_list
        self.name = name
        self.las2Cards = self._get_last_2_cards()

    def to_string(self) -> str:
        string = f"{self.name}: "
        for card in self.cards_list:
            string += card.to_string() + " "
        return string

    def shuffle_it(self) -> None:
        random.shuffle(self.cards_list)
        self.las2Cards = self._get_last_2_cards()

    def _get_last_2_cards(self) -> list[Card]:
        return [self.cards_list[len(self.cards_list)-2], self.cards_list[len(self.cards_list)-1]]

    def get_last_2_cards_as_string(self):
        txt = f"{self.name} last 2 cards: "
        for ending_card in self._get_last_2_cards():
            txt += ending_card.to_string() + " "
        txt += f"| sum = {self.get_sum_of_last_2_cards()}"
        return txt

    def get_sum_of_last_2_cards(self) -> int:
        return self.las2Cards[0].value + self.las2Cards[1].value


list_of_cards = []

for i in range(1, 10+1):
    list_of_cards.append(Card(str(i), i))
list_of_cards.append(Card("J", 11))
list_of_cards.append(Card("Q", 12))
list_of_cards.append(Card("K", 13))
list_of_cards.append(Card("A", 14))

d1 = Deck("My Deck ", list_of_cards)
d2 = Deck("Computer", list_of_cards.copy())

print(d1.to_string())
print(d2.to_string() + "\n")

d1.shuffle_it()
d2.shuffle_it()
print(d1.to_string())
print(d2.to_string() + "\n")

print(d1.get_last_2_cards_as_string())
print(d2.get_last_2_cards_as_string() + "\n")

if d1.get_sum_of_last_2_cards() > d2.get_sum_of_last_2_cards():
    print(f"{d1.name} wins")
elif d1.get_sum_of_last_2_cards() < d2.get_sum_of_last_2_cards():
    print(f"{d2.name} wins")
else:
    print("it's a draw")



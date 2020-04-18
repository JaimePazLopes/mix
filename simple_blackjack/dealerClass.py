import random
from src.playerClass import Player


class Dealer(Player):

    def __init__(self):
        super(Dealer, self).__init__(0)
        self.deck = list()
        self.showCard = False
        self.function = "Dealer"

    def useNewDeck(self, deck):
        self.deck = deck

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def distributeInicialCards(self, player):
        self.giveCard(player, 2)
        self.giveCard(self, 2)

    def hands(self):
        hand = ""
        for card in self.cards[:-1]:
            hand += str(card) + " "
        if self.showCard:
            hand += str(self.cards[-1])
        else:
            hand += "??"
        print(f"Dealer hand: " + hand)

    def giveCard(self, target, quantity=1):
        for index in range(quantity):
            target.drawCard(self.deck.pop())

    def resetState(self):
        self.chooseStay = False
        self.showCard = False

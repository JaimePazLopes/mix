from src.cardClass import Card
from src.dealerClass import Dealer
from src.playerClass import Player


class Game:

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = self.createDeck()
        self.startNewGame()

    def startNewGame(self):
        if self.player.chips < 10:
            print("The player doesnt have enough chips to bet... The House always win!!")
            return
        print("New game starting...")
        self.dealer.useNewDeck(self.deck.copy())
        print("The dealer is shuffling the cards.")
        self.dealer.shuffleDeck()
        print("The dealer distributes the cards.")
        self.dealer.distributeInicialCards(self.player)
        self.player.showChips()
        self.player.bet(10)
        print("The game beings...")
        self.gameLoop()

    def createDeck(self):
        deck = list()
        listOfValues = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        listOfSuits = ["♦","♣","♥","♠"]
        for value in listOfValues:
            for suit in listOfSuits:
                deck.append(Card(value,suit))
        return deck

    def gameLoop(self):
        self.dealer.hands()
        self.player.hands()
        while True:
            if self.checkHands(self.player) == 21:
                self.player.won(20)
                break
            if not self.player.chooseStay:
                print("What are you going to do? 1-Hit 2-Stay")
                inputValue = 0
                while inputValue not in ["1","2"]:
                    inputValue = input()
                if inputValue == '1':
                    self.player.hit()
                    self.dealer.giveCard(self.player)
                else:
                    self.player.stay()
                self.dealer.showCard = True
                self.dealer.hands()
                self.player.hands()
                if self.checkHands(self.player) == 21:
                    print("The Player got 21!!!!!")
                    self.player.won(20)
                    break
                if self.checkHands(self.player) > 21:
                    print("The Player Bust!!")
                    break
            #Dealer IA
            print("Dealers Turn")
            input()
            if self.player.chooseStay and self.checkHands(self.dealer) > self.checkHands(self.player):
                print("Dealer is closer to 21!!! The House always win!!")
                break
            elif self.player.chooseStay and self.checkHands(self.dealer) <= self.checkHands(self.player):
                self.dealer.hit()
                self.dealer.giveCard(self.dealer)
            elif self.checkHands(self.dealer) < 17:
                self.dealer.hit()
                self.dealer.giveCard(self.dealer)
            elif self.checkHands(self.dealer) < 21:
                if not self.dealer.chooseStay:
                    self.dealer.stay()
            self.dealer.hands()
            self.player.hands()
            #Delaer states
            if self.checkHands(self.dealer) == 21:
                print("Dealer got 21!!! The House always win!!")
                break
            elif self.checkHands(self.dealer) > 21:
                print("The Dealer Bust!!")
                self.player.won(20)
                break
        print("This game is over.")
        self.dealer.emptyHand()
        self.player.emptyHand()
        self.player.resetState()
        self.dealer.resetState()
        input()
        self.startNewGame()

    def checkHands(self, target):
        numberOfAces = 0
        sumCards = 0
        for card in target.cards:
            sumCards += card.realValue
            if card.realValue == 11:
                numberOfAces += 1
        if numberOfAces == 0:
            return sumCards
        for count in range(numberOfAces):
            if sumCards > 21:
                sumCards -= 10
            else:
                break
        return sumCards
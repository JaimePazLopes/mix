class Player:

    def __init__(self, chips = 100):
        self.chips = chips
        self.cards = list()
        self.chooseStay = False
        self.function = "Player"

    def bet(self, value):
        if value > self.chips:
            print("Player doesnt have that much chips.")
        self.chips -= value
        print(f"Player is betting {value} ©.")

    def won(self, value):
        self.chips += value
        print(f"Player won {value} ©")

    def stay(self):
        print(f"{self.function} choose Stay")
        self.chooseStay = True

    def hit(self):
        print(f"{self.function} choose Hit")

    def hands(self):
        hand = ""
        for card in self.cards:
            hand += str(card) + " "
        print(f"Player hand: " + hand)

    def drawCard(self, card):
        self.cards.append(card)

    def showChips(self):
        print(f"The Player has {self.chips} ©.")

    def emptyHand(self):
        self.cards = list()

    def resetState(self):
        self.chooseStay = False

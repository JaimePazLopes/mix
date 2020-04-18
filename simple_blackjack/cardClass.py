
class Card:

    def __init__(self, value, suit):
        if value not in [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]:
            print("Invalid value, must be 2 to 10, J, Q, K, A")
            value = 0
        if not(suit in ["♦","♣","♥","♠"] or suit in ["D","C","H","S"]):
            print("Invalid suit, must be one of those: ♦♣♥♠")
            suit = ""
        self.value = value
        self.suit = self.convertToSuit(suit)
        if value not in ["J","Q","K","A"]:
            self.realValue = value
        elif value in ["J","Q","K"]:
            self.realValue = 10
        else:
            self.realValue = 11

    def __str__(self):
        return str(self.value)+self.suit

    def convertToSuit(self, suit):
        if suit in ["♦","♣","♥","♠"]:
            return suit
        if suit == "D":
            return "♦"
        if suit == "C":
            return "♣"
        if suit == "H":
            return "♥"
        return "♠"

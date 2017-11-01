import math
import random

class Game(object):
    def __init__(self, name, playerCount):
        self.name = name
        self.count = playerCount
        self.discard = []
        self.players=[]
        self.dealNumer = 5
        self.deck = Deck()
        self.deck.shuffle()
        self.createPlayers()
        self.deck.displayInfo()
        self.displayPlayerInfo()
    def createPlayers(self):
        for i in range (1, self.count+1):
            name = "Player " + str(i)
            player = Player(name)
            player.deck = self.deck
            self.players.append(player)
    def displayPlayerInfo(self):
        for el in self.players:
            print el.name
            el.displayHand()
    def deal(self):
        print "Dealing {} cards".format(self.dealNumer) 
        for i in range(0, self.dealNumer):
            for player in self.players:
                temp = self.deck.cards.pop()
                print str(temp.suit) + " " + str(temp.value)
                player.hand.append(temp)      
        
class Deck(object):
    def __init__(self):
        self.cards = []
        self.create()
    def create(self):
        for i in range(1,5):
            for j in range(1,14):
                card = Card(i,j)
                self.cards.append(card)    
    def shuffle(self):
        print "Shuffling deck"
        for i in range(0,52):
            temp = self.cards[i]
            x = random.randint(0,51);
            self.cards[i] = self.cards[x]
            self.cards[x] = temp 
            
    def displayInfo(self):
        print "Display deck"
        cards = []
        for el in self.cards:
            temp = str(el.suit) + " " + str(el.value)
            cards.append(temp)
        print cards
        print len(cards)
    
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []
        self.deck = None
    def draw(self):
        print "Drawing from the deck"
        self.hand.append(self.deck.cards.pop())
    def displayHand(self):
        cards = []
        for el in self.hand:
            temp = str(el.suit) + " " + str(el.value)
            cards.append(temp)
        print cards
       
print "Welcome to the Game of Cards"
print "Choose from options"
print "1. Go Fish"

gameName = raw_input("Choose you game : ")

playerCount =  int(raw_input("Choose the number of player (2-2): "))

print "Game name {} and number of players {}".format(gameName, playerCount)

game = Game(gameName, playerCount)

print "1. Deal"

dealValue = int(raw_input("Choose your input : "))

game.deal()
game.displayPlayerInfo()
game.deck.displayInfo()
game.players[0].draw()
game.players[1].draw()
game.displayPlayerInfo()
game.deck.displayInfo()

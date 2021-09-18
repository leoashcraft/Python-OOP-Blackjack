import random

class BlackJack:
    def __init__(self):
        self.cards = []
        self.clubs = []
        self.diamonds = []
        self.hearts = []
        self.spades = []
        self.suits = (self.clubs, self.diamonds, self.hearts, self.spades)
        self.suitNames = ("clubs", "diamonds", "hearts", "spades")
        self.cardsDictionary = {}   # 1 : '1 clubs'
        self.totalDealerCards = 0
        self.totalPlayerCards = 0

        print("Computer is the dealer while you are the player")

        # join all suits together
        count = -1
        for suit in self.suits:
            count = count + 1
            for num in range(1, 14):
                cardName = str(num) + " " + self.suitNames[count]
                suit.append(cardName)
                self.cardsDictionary[cardName] = num
            self.cards = self.cards + suit

        print("There are",len(self.cards), "cards")
        print(self.cardsDictionary)

    # generate random cards
    def randomCards(self):
        return random.sample(self.cards, 1)

    # calculate sum of dealer's and player's cards
    def cardTotal(self):
        self.totalDealerCards = 0
        for singleDealerCard in self.dealerCards:
            self.totalDealerCards = self.totalDealerCards + self.cardsDictionary[singleDealerCard]
        
        self.totalPlayerCards = 0
        for singlePlayerCard in self.playerCards:
            self.totalPlayerCards = self.totalPlayerCards + self.cardsDictionary[singlePlayerCard]

    # check who wins 
    def checkWinner(self, s = None):
        # if player enters 's'
        if s == "s":
            print("Dealer cards are", self.dealerCards, " = ", self.totalDealerCards)
            print("Your cards are", self.playerCards, " = ", self.totalPlayerCards)
            if self.totalDealerCards > self.totalPlayerCards:
                print("Game over!\nDealer wins")
                return "Dealer wins"
            elif self.totalPlayerCards > self.totalDealerCards:
                print("Game over!\nYou win")
                return "You win"

        # is sum of dealer's or player's cards equal to 21, if so return winner
        self.cardTotal()
    
        if self.totalPlayerCards == 21:
            print("Blackjack!", "You win")
            return "You win"
        return "No winner"

    # start game
    def start(self):
        print("Game has started")
        self.dealerCards = []
        self.playerCards = []

        # generate 2 random cards each for the dealer and the player
        for cardLoop in [self.dealerCards, self.playerCards]:
            for _ in range(2):
                cardLoop.append(self.randomCards()[0])
        print("Cards have been dealed for you and the dealer")
        self.cardTotal()
        print("Dealer's cards are", [self.dealerCards[0], "hidden"])
        print("Your cards are", self.playerCards, " = ", self.totalPlayerCards)

        # check if dealer's or player's cards are up to 21 and anounce winner 
        winner = self.checkWinner()
        
        while winner == "No winner":
            playerInput = input("Enter h to hit, Enter s to stand:\n")
            if playerInput == "h":
                print("New card has been dealed for you")
                self.playerCards.append(self.randomCards()[0])
                self.cardTotal()
                print("Your cards are", self.playerCards, " = ", self.totalPlayerCards)
            elif playerInput == "s":
                self.checkWinner("s")
                break

            self.cardTotal()
            if (self.totalDealerCards < 21) or (self.totalDealerCards >= 21):
                self.dealerCards.append(self.randomCards()[0])
                self.cardTotal()
                print("Dealer just dealed a new card for itself")

                

b = BlackJack()
b.start()




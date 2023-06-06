import random

#BlackJack
    #Coded by David Cui
    #Excercise guided by FreeCodeCamp

class Card:
    def __init__(self, suit, rank):
         self.suit = suit
         self.rank = rank
    def __str__(self):
        #This method will print is envoked from the class
        return f"{self.rank['rank']} of {self.suit}"
                #F strings are the best way to code combining both
                #Strings as well as objects in CS

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]    
        ranks = [
                {"rank": "A", "value": 11},
                {"rank": "2", "value": 2},
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "K", "value": 10},
            ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        
    def shuffle(self):
        #The deck doesn't need to be shuffled in there is only one card
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0: #needs to be len() 
                card = self.cards.pop()   
                cards_dealt.append(card)
        return cards_dealt

class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
        
    def addCard(self, card_list):
        self.cards.extend(card_list)
           
    def calculate_Value(self):
        self.value = 0
        has_Ace = False
        
        for card in self.cards:
            self.value += int(card.rank["value"])
            if card.rank["rank"] == "A":
                has_Ace = True
        
        if has_Ace and self.value > 21:
                self.value -= 10 
    
    def getValue(self):
        self.calculate_Value()
        return self.value
    
    def isBlackJack(self):
        return self.getValue() == 21
            
    def display(self, show_dealer_cards = False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
            and not show_dealer_cards \
            and not self.isBlackJack():
                print("hidden")
            else:
                print(card)
            
        if not self.dealer:
            print("Value:", self.getValue())
        print()
            
class Game:
    def play(self):
        game_number = 0
        games2play = 0
        
        while games2play <= 0:
            try:
                games2play = int(input("How many games do you want to play? "))
            except:
                print("You must put in a number")
        
        while game_number < games2play:
            game_number += 1
            deck = Deck()
            deck.shuffle()
            
            player_hand = Hand()
            dealer_hand = Hand(dealer = True)
            
            for x in range(2):
                player_hand.addCard(deck.deal(1))
                dealer_hand.addCard(deck.deal(1))
                
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games2play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()
            
            if self.check_winner(player_hand, dealer_hand):
                continue
        
            choice = ""
            while player_hand.getValue() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choost 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "s", "stand", "hit"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S)").lower()
                    print()
                if choice in ['hit', 'h']:
                    player_hand.addCard(deck.deal(1))
                    player_hand.display()
            
            if self.check_winner(player_hand, dealer_hand):
                continue
        
            player_hand_value = player_hand.getValue()
            dealer_hand_value = dealer_hand.getValue()
        
            while dealer_hand_value < 17:
                dealer_hand.addCard(deck.deal(1))
                dealer_hand_value = dealer_hand.getValue()
            
            dealer_hand.display(show_dealer_cards= True)
        
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer hand:", dealer_hand_value)
            
            self.check_winner(player_hand, dealer_hand, True)
            
        print("\nThanks for playing!")
                
    def check_winner(self, player_hand, dealer_hand, game_over = False):
        if not game_over:
            if player_hand.getValue() > 21:
                print("You lost, Dealer wins")
                return True
            elif dealer_hand.getValue() > 21:
                print("You won! Dealer lost.")
                return True
            elif dealer_hand.isBlackJack() and player_hand.isBlackJack():
                print("Both players have Blackjack! Tie.")
                return True
            elif player_hand.isBlackJack():
                print("You won! BlackJack!")
                return True
            elif dealer_hand.isBlackJack():
                print("Dealer won! You lost.")
                return True
        else:
            if player_hand.getValue() > dealer_hand.getValue():
                print("You win!")
            elif player_hand.getValue() == dealer_hand.getValue():
                print("Tie. --.--")
            else:
                print("Dealer wins.")
                return True
        return False


g = Game()
g.play()

#BlackJack Program - Day 13

#Importing modules
import random

#Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

#Card Class
class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return self.rank + " of " + self.suit

#print(Card(suits[0],ranks[0]))

#Deck Class
class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

# new_deck = Deck()
# for card in new_deck.deck:
# 	print(card)
	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp = deck_comp + " "+ card.__str__() + ","
		return "The deck has:" + deck_comp


	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()


#Hand Class
class Hand:
	def __init__(self):
		self.card = []
		self.value = 0
		self.aces = 0
	def add_card(self,card):
		self.card.append(card)
		self.value = self.value + values[card.rank]
		if card.rank == 'Ace':
			self.aces = self.aces + 1
	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value = self.value - 10
			self.aces = self.aces - 1 

# test_deck = Deck()
# test_deck.shuffle()
# #print(Deck())
# in_Hand = Hand()
# in_Hand.add_card(test_deck.deal())
# in_Hand.add_card(test_deck.deal())
# in_Hand.add_card(test_deck.deal())
# print(in_Hand.value)
# for card in in_Hand.card:
# 	print(card)

#Chips class to keep track of player chips
class Chips:
	def __init__(self):
		self.total = 100
		self.bet = 0
	def win_bet(self):
		pass
	def lose_bet(self):
		pass

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet?"))
		except ValueError:
			print("Please enter an integer")
		else:
			if chips.bet > chips.total:
				print("Your bet cant exceed", chips.total)
			else:
				break


def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing
	while True:
		x = input("Would you like to take Hit 'h' or Stand 's'?")
		if x[0].lower()=='h':
			hit(deck,hand)
		elif x[0].lower()=='s':
			print("Player stands. Dealer is playing")
			playing = False
		else:
			print("Sorry, please try again")
			continue
		break
def show_some(player,dealer):
	print("Dealer's hands: Card hidden, ",dealer.cards[1])
	print("Player's cards: ", player.cards)
def show_all(player,dealer):
	print("Dealer's hand:", dealer.cards, " - ", dealer.value)
	print("Player's hand:", player.cards, " - ", player.value)




#Game Scenarios
def player_busts(player,dealer,chips):
	print("Player busts!")
	chips.lose_bet()
def player_wins(player,dealer,chips):
	print("Player wins!")
	chips.win_bet()  
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.lose_bet() 
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.win_bet()   
def push(player,dealer):
	print("Player and dealer tie!")

#Game Logic


while True:
    # Print an opening statement
    print("Welcome to Game of Black Jack!")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
       
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
        	player_busts(player_hand,dealer_hand, player_chips)
        	break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value<21:
    	while deal.hand.value<17:
    		hit(deck,dealer_hand)
    	#Show all cards
    	show_all(player_hand,dealer_hand)
    	# Run different winning scenarios
    	if dealer_hand.value > 21:
    		dealer_busts(player_hand,dealer_hand,player_chips)
    	elif dealer_hand.value > player_hand.value:
    		dealer_wins(player_hand,dealer_hand,player_chips)
    	elif dealer_hand.value < player_hand.value:
    		player_wins(player_hand,dealer_hand,player_chips)
    	else:
    		push(player_hand,dealer_hand)   
    
    # Inform Player of their chips total 
    print("Player has total chips :" + player_chips.total)
    
    # Ask to play again
    play_again = input("Like to play again? ")
    if play_again[0].lower() == 'y':
    	playing = True
    	continue
    else:
    	playing = False
    	print("Thanks for playing")
    	break

    


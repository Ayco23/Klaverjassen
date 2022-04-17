
import random
from itertools import cycle

class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards = []
    def __repr__(self):
        return f'{self.name}'


    def play_card(self, card):
        self.cards.remove(card)
        return card
    
    def sort_card(self):
        self.cards = sorted(self.cards, key = lambda card: (card.suit, card.strength))


class Card:
    def __init__(self, value: str, suit: str, strength: int = 0, points: int = 0):
        self.value = value
        self.suit = suit
        self.points = points
        self.strength = strength
        self.x = 0
        self.y = 0
    
    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Game():
    def __init__(self, name: str, players: list[Player] = [Player("p1"), Player("p2"), Player("p3"), Player("p4")]):
        self.name = name
        self.deck = self.create_deck_small()
        self.players = players
        self.current_player = self.players[0]
        self.table = []

    def create_deck_default(self):
        # Make an empty list
        deck = []
        
        for n in range(4):

            # Define the suit of the cards
            if n == 0:
                suit = 'Hearts'
            elif n == 1:
                suit = 'Clubs'
            elif n == 2:
                suit = 'Spades'
            elif n == 3:
                suit = 'Diamonds'
            
            # Create and append the cards with digits
            for n in range(9):
                deck.append(Card(str(n + 2), suit))
            
            # Create and append the 'special' cards
            deck.append(Card('Jack', suit))
            deck.append(Card('Queen', suit))
            deck.append(Card('King', suit))
            deck.append(Card('Ace', suit))

        # Return the deck
        return deck

    def create_deck_small(self):
        # Make an empty list
        deck = []
        
        for n in range(4):

            # Define the suit of the cards
            if n == 0:
                suit = 'Hearts'
            elif n == 1:
                suit = 'Clubs'
            elif n == 2:
                suit = 'Spades'
            elif n == 3:
                suit = 'Diamonds'
            
            # Create and append the cards
            deck.append(Card('7', suit, -1))
            deck.append(Card('8', suit, 0))
            deck.append(Card('9', suit, 1))
            deck.append(Card('Jack', suit, 2))
            deck.append(Card('Queen', suit, 3))
            deck.append(Card('King', suit, 4))
            deck.append(Card('10', suit, 10))
            deck.append(Card('Ace', suit, 11))

        # Return the deck
        return deck
    
    def next_player(self):
        # Find the index of the current player
        for i, player in enumerate(self.players):
            if player == self.current_player:
                index = i
        
        # Set the index to the next player
        self.current_player = self.players[(index + 1) % len(self.players)]

        print(f"Current player is now {self.current_player.name}")
    
    def shuffle(self):
        print('Shuffling deck...')
        random.shuffle(self.deck)

    def deal_card(self, amount_of_cards: int) -> list:
        cards = []
        for i in range(amount_of_cards):
            cards.append(self.deck.pop(0))
        return cards

    def deal(self):
        # Shuffle the deck
        self.shuffle()

        # Deal each player 3, then 2, then 3 cards...
        for player in self.players:
            dealed = self.deal_card(3)
            for card in dealed:
                player.cards.append(card)
        for player in self.players:
            dealed = self.deal_card(2)
            for card in dealed:
                player.cards.append(card)
        for player in self.players:
            dealed = self.deal_card(3)
            for card in dealed:
                player.cards.append(card)
                # When all cards are taken, sort the cards of each player
                player.sort_card()

    def get_card(self, card):
        self.table.append(self.current_player.play_card(card))
        self.next_player()    
    

def main():
    p1 = Player('Ayco')
    p2 = Player('Emiel')
    p3 = Player('Joep')
    p4 = Player('Angelique')
    players = [p1, p2, p3, p4]


    g = Game('kaarten', players)


    


    






if __name__ == '__main__':
    main()
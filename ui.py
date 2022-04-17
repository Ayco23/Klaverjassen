import pygame as pg
from main import Player, Card, Game


class PygameUI:
    def __init__(self) -> None:
        self.IMAGES = {}
        self.game = Game("Klaverjassen")
        self.screen_size = (1280, 780)
        self.screen = pg.display.set_mode(self.screen_size)
        pg.display.set_mode(self.screen_size)
        pg.init()
        pg.display.set_caption("klaverjassen")
        self.load_images()
        self.font = pg.font.Font('freesansbold.ttf', 32)
    

    def mainloop(self):
        running = True
        while running:
            self.screen.fill("dark green")
            self.draw_deck()
            self.draw_players()
            self.draw_table()
            self.screen.blit(self.IMAGES['shuffle_button'], (700, 500))
            self.screen.blit(self.IMAGES['deal_button'], (200, 500))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                
                # Checks whether left-mouse is clicked
                if event.type == pg.MOUSEBUTTONUP:
                    mouselocation = pg.mouse.get_pos()

                    # Shuffle is clicked
                    if self.IMAGES['shuffle_button'].get_rect(x = 700, y =  500).collidepoint(event.pos):
                        self.game.shuffle()
                        print("shuffle deck")
                    # Deal is clicked
                    if self.IMAGES['deal_button'].get_rect(x = 200, y =  500).collidepoint(event.pos):
                        self.game.deal()
                        print("Dealing cards...")
                    
                    # current player plays a card
                    for card in self.game.current_player.cards:
                        if self.IMAGES[card].get_rect(x = card.x, y =  card.y).collidepoint(event.pos):
                                print(f"The {card} from {self.game.current_player} is clicked!")
                                self.game.get_card(card)
                                print(f"Table = {self.game.table}")

                    # any player clicks their card
                    for player in self.game.players:
                        for card in player.cards:
                            if self.IMAGES[card].get_rect(x = card.x, y =  card.y).collidepoint(event.pos):
                                print(f"The {card} from {player.name} is clicked!")

                pg.display.flip()

    def load_images(self):
        # load buttons
        self.IMAGES['shuffle_button'] = pg.image.load("sprites/shuffle_button.png")
        self.IMAGES['deal_button'] = pg.image.load("sprites/deal_button.png")

        # load cards
        for card in self.game.deck:
            img = f"{card.value}_of_{card.suit}"
            self.IMAGES[card] = pg.image.load("sprites/cards/"+ img +".png")
            self.IMAGES[card] = pg.transform.scale(self.IMAGES[card], (50, 73))

        
    def draw_deck(self):
        x = 100
        y = 100
        for card in self.game.deck:
            self.screen.blit(self.IMAGES[card], (x, y))
            x += 50
    
    def draw_players(self):
        x = 100
        y = 100
        for player in self.game.players:
            self.screen.blit(self.font.render(player.name, True, "black"), (x, y))
            x_card = 100
            for card in player.cards:
                card.x = x + x_card
                card.y = y
                self.screen.blit(self.IMAGES[card], (card.x, card.y))
                x_card += 60

            #x += 100
            y += 100
    
    def draw_table(self):
        x = 800
        x_card = 0
        y = 350
        self.screen.blit(self.font.render("Table", True, "black"), (x, y - 50))
        for card in self.game.table:
            card.x = x + x_card
            card.y = y
            self.screen.blit(self.IMAGES[card], (card.x, card.y))
            x_card += 60

        


def main():
    ui = PygameUI()
    ui.mainloop()

if __name__ == '__main__':
    main()
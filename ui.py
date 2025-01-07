import pygame

class UI:
    def __init__(self,surface):

        # setup
        self.display_surface = surface

        # coins
        self.coin = pygame.image.load('./graphics/ui/coin.png')
        self.coin_rect = self.coin.get_rect(topleft = (20,41))
        self.font = pygame.font.Font('./graphics/ui/MANIA.ttf',30)

    def show_coins(self,amount):
        self.display_surface.blit(self.coin,self.coin_rect)
        coin_amount_surf = self.font.render(str(amount),False,'#FFD700')
        coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right + 4,self.coin_rect.centery))
        self.display_surface.blit(coin_amount_surf,coin_amount_rect)

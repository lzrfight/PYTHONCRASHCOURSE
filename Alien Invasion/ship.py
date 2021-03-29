# Copyright 2021/3/29 LI ZHUORAN. All rights reserved.
import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('/Users/lizhuoran/desktop/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 2
        if self.moving_left:
            self.rect.centerx -= 2

    def blitme(self):
        self.screen.blit(self.image, self.rect)

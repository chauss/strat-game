'''
Created on 13.04.2014

@author: Chris
'''
import pygame
import gui_utils as utils


class GameMenu(object):
    def __init__(self):
        pygame.init()
        
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("StratGame")
    
        pygame.mouse.set_visible(1)
        pygame.key.set_repeat(1, 30)
        
        clock = pygame.time.Clock()
        screen.fill((0, 0, 0))
        
        image = utils.import_image("fire_and_ice.jpg")
        
        running = 1
        while running:
            clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))
                    if event.key == pygame.K_w:
                        screen.fill((255, 255, 255))
                    if event.key == pygame.K_b:
                        screen.fill((0, 0, 0))
                    if event.key == pygame.K_p:
                        screen.blit(image, (0, 0))
                
            pygame.display.flip()
    
    
gm = GameMenu()


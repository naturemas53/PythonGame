
import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Resources/intro_ball.gif")
ballrect = ball.get_rect()

font2 = pygame.font.SysFont(None, 50)
text2 = font2.render("hello, world", True, (255,255,255))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(text2, (0,0));

    pygame.display.flip()
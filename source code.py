import pygame
import random
pygame.init()
a=random.randint(0,255)
b=random.randint(0,255)
c=random.randint(0,255)
white = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
color= (a,b,c)
scr = pygame.display.set_mode((3000, 2500))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scr.fill((2, 55, 42))
    pygame.draw.circle(scr, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (random.randint(0,255), random.randint(0,255)), random.randint(0,255))
    pygame.draw.circle(scr, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (random.randint(0,255), random.randint(0,255)), random.randint(0,255))
    pygame.draw.circle(scr, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (random.randint(0,255), random.randint(0,255)), random.randint(0,255))
    pygame.draw.rect(scr, color, pygame.Rect(random.randint(0,999), random.randint(0,999), random.randint(0,999), random.randint(0,999)))
    pygame.draw.rect(scr, color, pygame.Rect(random.randint(0,999), random.randint(0,999), random.randint(0,999), random.randint(0,999)))
    pygame.draw.rect(scr, color, pygame.Rect(random.randint(0,999), random.randint(0,999), random.randint(0,999), random.randint(0,999)))
    pygame.draw.ellipse(scr, white , (random.randint(0,999), random.randint(0,999), random.randint(0,999), random.randint(0,999)), random.randint(0,999))
    pygame.display.flip()
pygame.quit()

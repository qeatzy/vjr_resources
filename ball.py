import pygame
pygame.init()
screen=pygame.display.set_mode((700,500))
print(screen)

im=pygame.image.load("ball.gif")
screen.blit(im,im.get_rect())
pygame.display.update()



print(im)
running=True
while running:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                running=False

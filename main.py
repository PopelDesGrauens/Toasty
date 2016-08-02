import pygame
from pygame.locals import*

screen = pygame.display.get_surface()

black = (0,0,0)
white = (255, 255, 255)
display = (1280,720)
w =640
h =480
screen = pygame.display.set_mode((w, h))
pygame.display.toggle_fullscreen()
pygame.init()
pygame.mixer.init()
toastysound= pygame.mixer.Sound("TOASTY!.wav")

img = pygame.image.load('toastyguy.jpg')
img = pygame.transform.scale(img, (w, h))


running = 1
try:
    while running:
        screen.fill ((black))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    toastysound.play()
                    screen.fill((white))
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    screen.fill((black))
                    pygame.display.flip()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()



    pygame.quit()
except SystemExit:
    pygame.quit()
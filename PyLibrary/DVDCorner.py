import sys, time, pygame

    
def main():
    pygame.init()
    width, height = 800, 600
    dvdLogoSpeed = [2, 2]
    backgroundColor = 0, 0, 0

    screen = pygame.display.set_mode((width, height))

    dvdLogo = pygame.image.load("dvd-logo-white.png")
    dvdLogoRect = dvdLogo.get_rect()
    pygame.display.set_caption("DVD Corner")
    pygame.display.set_icon(dvdLogo)

    while True:
        pygame.event.get()
        screen.fill(backgroundColor)
        
        screen.blit(dvdLogo, dvdLogoRect)
        dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

        if dvdLogoRect.left < 0 or dvdLogoRect.right > width:
            dvdLogoSpeed[0] = -dvdLogoSpeed[0]
        if dvdLogoRect.top < 0 or dvdLogoRect.bottom > height:
            dvdLogoSpeed[1] = -dvdLogoSpeed[1]

        pygame.display.flip()
        time.sleep(10 / 1000)

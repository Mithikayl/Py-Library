import sys, time

    
def main():
    pygame.init()
    width, height = 800, 600
    dvdLogoSpeed = [2, 2]
    backgroundColor = 0, 0, 0

    screen = pygame.display.set_mode((width, height))

    dvdLogo = pygame.image.load("dvd-logo-white.png")
    dvdLogoRect = dvdLogo.get_rect()

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

if __name__ == "__main__":
    try:
        import pygame
    except ImportError:
        print("You need to have the module pygame to run this program.")
        choice = input("Install PyGame? (Y/N)\n").lower()
        if choice == "y":
            import os
            os.system('pip install --user pygame')
        if choice == "n":
            print("Exiting.")
            sys.exit()
        else:
            print("Invalid choice. Exiting program.")
            sys.exit()
    main()
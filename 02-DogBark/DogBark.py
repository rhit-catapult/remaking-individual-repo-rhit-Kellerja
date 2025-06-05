import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    image = pygame.image.load("2dogs.JPG")
    image = pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))
    # Prepare the text caption(s)
    # TODO 4: Create a font object with a size 28 font.
    font1 = pygame.font.SysFont("comicsansms", 28)
    print(pygame.font.get_fonts())
    myfonts = pygame.font.get_fonts()
    for afont in sorted(myfonts):
        print(afont)
    caption1 = font1.render("Hold up, let him cook", True, BLACK)

    font2 = pygame.font.SysFont("arial", 28)
    caption2 = font2.render("bottom text", True, WHITE)
    # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).

    # Prepare the music
    # TODO 8: Create a Sound object from the "bark.wav" file.
    bark_sound = pygame.mixer.Sound("bark.wav")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()
            # TODO 9: Play the music (bark) if there's a mouse click.

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(image, (0,0))
        # Draw the text onto the screen
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        x_loc = screen.get_width() / 2 - caption1.get_width() / 2
        x_loc2 = screen.get_width() / 2 - caption2.get_width() / 2
        y_loc = image.get_height() - 5
        screen.blit(caption1, (x_loc, y_loc))
        screen.blit(caption2, (x_loc2,0))
        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()

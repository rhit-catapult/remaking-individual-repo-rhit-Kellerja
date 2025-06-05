
import pygame
import sys


pygame.init()


pygame.display.set_caption("Jacob Keller")
# TODO 00: Change the window caption to say your name.


screen = pygame.display.set_mode((400, 600))
# TODO 05: Change the window size, make sure your circle code still works.


while True:

    for event in pygame.event.get():

        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events

    screen.fill(pygame.Color("Gray"))

    # Draw things on the screen

    # TODO 02: Try to draw a circle (any size, any color, anywhere)
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, pygame.Color("Orange"), (200, 450), 50 )

    # TODO 03: Try to draw a red circle in the middle of the screen with a radius 100
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, pygame.Color("Red"), (200, 300), 100 )

    # TODO 04: Try to draw a yellow circle with the center exactly in the lower left corner of the screen, radius 10
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, pygame.Color("Yellow"), (0, 600), 10 )

    # This will make sure that things appear on our screen, without this
    # update, everything we do will not be visible!
    # notice how this statement is still inside of the first while loop, but
    # outside of the for loop (why? because it is at the same level of
    # indentation as the for loop statement).
    pygame.display.update()

import pygame
import sys
import time
import random

class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """




        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0

    def draw(self):
        """ Draws this sprite onto the screen. """

        # self.screen.blit(self.image_no_umbrella, (self.x,self.y))




        if time.time() > self.last_hit_time + 0.1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """

        hit_box = pygame.Rect(self.x, self.y, self.image_umbrella.get_width(), self.image_umbrella.get_height())
        return hit_box.collidepoint(raindrop.x, raindrop.y)


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """


        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []


    def draw(self):
        """ Draws this sprite onto the screen. """

        self.screen.blit(self.image, (self.x, self.y))


    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """



        new_drop = Raindrop(self.screen, random.randint(self.x, self.x + self.image.get_width()), self.y + self.image.get_height() -8)
        self.raindrops.append(new_drop)

if __name__ == "__main__":
    print("being run, do some development")
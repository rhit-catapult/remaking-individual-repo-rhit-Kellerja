import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

class Ball:
    def __init__(self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed_x = random.randint(1,50)
        self.speed_y = random.randint(1,50)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x,self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x + self.radius > self.screen.get_width():
            self.speed_x *= -1
        if self.x - self.radius < 0:
            self.speed_x *= -1
        if self.y + self.radius > self.screen.get_height():
            self.speed_y *= -1
        if self.y - self.radius < 0:
            self.speed_y *= -1
# TODO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 640))
    pygame.display.set_caption('Bouncing Ball')
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1
    ball1 = Ball(screen, (0,0,0), 200, 10, 10, 10, 10)

    balls = []
    for k in range(99):
        ball2 = Ball(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                     random.randint(10, 300), random.randint(10, 300), random.randint(1, 50), random.randint(1, 50),
                     random.randint(1, 50))

        balls.append(ball2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball

        # TODO: Draw the ball
        ball1.draw()
        ball1.move()
        for k in range(99):
            balls[k].draw()
            balls[k].move()
        pygame.display.update()




main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball

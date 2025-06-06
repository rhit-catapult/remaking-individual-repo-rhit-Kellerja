import pygame
import sys
import time
import hero_module
import cloud_module
import raindrop_module

def main():


    pygame.init()
    pygame.display.set_caption("Es Regnet")
    screen = pygame.display.set_mode((1000,600))


    clock = pygame.time.Clock()

    # test_drop = Raindrop(screen, 320, 10)


    mike = hero_module.Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    alyssa = hero_module.Hero(screen, 700,400, "Alyssa_umbrella.png", "Alyssa.png")


    cloud = cloud_module.Cloud(screen, 300, 50,"another_cloud.png")
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()






        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 10
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 10
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 10
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += 10


        screen.fill(pygame.Color("White"))
        # --- begin area of test_drop code that will be removed later

        # test_drop.move()

        # if test_drop.off_screen():
        #     test_drop.y = 10
        # test_drop.draw()

        # if mike.hit_by(test_drop):
        #     mike.last_hit_time = time.time()


        # if alyssa.hit_by(test_drop):
        #     alyssa.last_hit_time = time.time()





        # --- end area of test_drop code that will be removed later


        cloud.draw()



            #       - move the Raindrop.
            #       - draw the Raindrop.

        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.


        mike.draw()
        alyssa.draw()

        pygame.display.update()


main()
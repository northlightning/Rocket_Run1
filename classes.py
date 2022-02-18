import pygame as pg
from settings import *
from random import randrange


class Star(pg.sprite.Sprite):
    def __init__(self, image):
        super(Star, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x = randrange(0, (WIN_WIDTH + 1) - self.rect.w)
        self.rect.y = -self.rect.h
        self.speed = 0

    def update(self, speed):
        self.speed = speed
        self.rect.y += self.speed


class Rocket:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pg.image.load("rocketFireMiddle.png")
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.state = "Idle"
        self.AnimIdx = 0
        self.rocketCounter = 0
        self.kilometers = 0
        self.speed = 3
        self.speed_timer = 0

        self.AnimMiddle = []
        self.AnimMiddle.append(pg.image.load("rocketFireMiddle.png"))
        self.AnimMiddle.append(pg.image.load("rocketFireRight.png"))
        self.AnimMiddle.append(pg.image.load("rocketFireMiddle.png"))
        self.AnimMiddle.append(pg.image.load("rocketFireLeft.png"))

        self.AnimToRight = []
        self.AnimToRight.append(pg.image.load("rocketFireLeft.png"))
        self.AnimToRight.append(pg.image.load("rocketFireFlyRight.png"))

        self.AnimToLeft = []
        self.AnimToLeft.append(pg.image.load("rocketFireRight.png"))
        self.AnimToLeft.append(pg.image.load("rocketFireFlyLeft.png"))

    def update(self):
        if self.rocketCounter == 10:
            self.AnimIdx += 1
            self.kilometers += 1
            self.speed_timer += 1
        if self.rocketCounter > 10:
            self.rocketCounter = 0
        if self.speed_timer >= 100:
            self.speed_timer = 0
            self.speed = randrange(2, 6)

        self.rocketCounter += 1

    def animation(self):
        if self.state == "Idle":
            if self.AnimIdx > 3:
                self.AnimIdx = 0
            self.screen.blit(self.AnimMiddle[self.AnimIdx], (self.x, self.y))
            self.image = self.AnimMiddle[self.AnimIdx]
        if self.state == "ToRight":
            if self.AnimIdx > 1:
                self.AnimIdx = 0
            self.screen.blit(self.AnimToRight[self.AnimIdx], (self.x, self.y))
            self.image = self.AnimToRight[self.AnimIdx]
        if self.state == "ToLeft":
            if self.AnimIdx > 1:
                self.AnimIdx = 0
            self.screen.blit(self.AnimToLeft[self.AnimIdx], (self.x, self.y))
            self.image = self.AnimToLeft[self.AnimIdx]

    def collision(self, star):
        offset = (star.rect.x - self.x, star.rect.y - self.y)
        return self.mask.overlap(star.mask, offset)


class StarSpawner:
    def __init__(self):
        self.group = pg.sprite.Group()
        self.spawn_timer = randrange(30, 120)

    def update(self, star_speed):
        self.group.update(star_speed)
        if self.spawn_timer == 0:
            self.spawn()
            self.spawn_timer = randrange(30, 120)
        else:
            self.spawn_timer -= 1
        for star in self.group:
            if star.rect.y > WIN_HEIGHT:
                self.group.remove(star)

    def spawn(self):
        new_star = Star(STAR_IMGS[randrange(4)])
        self.group.add(new_star)


class Score:
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.font = pg.font.Font('c:/Windows/fonts/impact.ttf', 30)
        self.text = self.font.render("0", True, [247, 176, 22])
        self.kilometers = 0

    def draw(self):
        self.screen.blit(self.text, (self.x, self.y))

    def update(self, kilometers):
        self.kilometers = kilometers
        self.text = self.font.render(str(self.kilometers), True, [247, 176, 22])

from pygame import*
from random import*
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("cucumber_PNG84293 (1).png", self.rect.x-25, self.rect.y, 4)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        global i
        global p
        global babka
        self.rect.y += self.speed
        if self.rect.y >= 510:
            self.rect.y = 0
            self.rect.x = randint(50, 650)
            i += 1
class Meteor(GameSprite):
    def update(self):
        global p
        global babka
        self.rect.y += self.speed
        if self.rect.y >= 510:
            self.rect.y = 0
            self.rect.x = randint(50, 650)
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
i = 0
p = 0
font.init()
font1 = font.SysFont(None, 36)
font2 = font.SysFont(None, 70)
win_width = 700
win_height = 500
babka = Player("angry-old-woman.jpg", 50, 420, 8)
monster1 = Enemy("2.png", 50, 0, 2)
monster2 = Enemy("2.png", 150, 0, 2)
monster3 = Enemy("2.png", 270, 0, 2)
monster4 = Enemy("2.png", 350, 0, 2)
monster5 = Enemy("2.png", 550, 0, 2)
meteor1 = Meteor("tomato_PNG12599.png", 100, 0, 1)
meteor2 = Meteor("tomato_PNG12599.png", 250, 0, 1)
meteor3 = Meteor("tomato_PNG12599.png", 400, 0, 1)
meteors = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)
meteors.add(meteor1)
meteors.add(meteor2)
meteors.add(meteor3)
win = display.set_mode((win_width, win_height))
background = transform.scale(image.load("pirozhoksmjasom.jpg-600x410.jpg"),(win_width, win_height))
#clock = clock.Clock()
game = True
finish = True
num_fire = 0
couldown = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if couldown == False and num_fire < 6:
                    num_fire += 1
                    babka.fire()
                if couldown == False and num_fire >= 6:
                    couldown = True
                    num_time = timer()
    if finish:
        display.update()
        win.blit(background,(0,0))
        babka.reset()
        babka.update()
        bullets.draw(win)
        bullets.update()
        monsters.draw(win)
        monsters.update()
        meteors.draw(win)
        meteors.update()
        if couldown == True:
            rel_time = timer()
            if rel_time - num_time < 1.5:
                text_pon = font1.render(
                    ("Перезарядка!"), 1, (100, 0, 0)
                )
                win.blit(text_pon, (260, 460))
            else:
                num_fire = 0
                couldown = False

        text_lose = font1.render(
            ("Пропущено: "+str(i)), 1, (0, 0, 0)
        )
        text_score = font1.render(
            ("Счёт: "+str(p)), 1, (0, 0, 0)
        )
        sptites_list = sprite.spritecollide(babka, monsters, False)
        if sprite.spritecollide(babka, monsters, False) or sprite.spritecollide(babka, meteors, False):
            babka.kill()
            i += 2
        groups_list = sprite.groupcollide(bullets, monsters, True, True)
        for z in groups_list:
            p += 1
            monster = Enemy("2.png", randint(0, 650), 0, 2)
            monsters.add(monster)
        win.blit(text_lose,(20,20))
        win.blit(text_score,(20,60))
        time.delay(20)
        if p >= 20:
            text_win = font1.render(
                ("Ты выиграл!"), 1, (0, 0, 0)
            )
            finish = False
            win.blit(text_win,(200,225))
        if i >= 5:
            text_false = font1.render(
                ("Ты проиграл!"), 1, (0, 0, 0)
            )
            finish = False
            win.blit(text_false,(200,225))
    display.update()
    #clock.tick(60)

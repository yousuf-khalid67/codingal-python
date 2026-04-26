import pygame
import random
import math
import time

pygame.init()

# Screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survive the Zombies")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# Colors (Zombie Theme)
BLACK = (15, 15, 15)
GREEN = (0, 200, 0)
RED = (180, 0, 0)
DARK_RED = (120, 0, 0)
PURPLE = (150, 0, 150)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


# ================= PLAYER =================
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = 20
        self.speed = 5
        self.health = 100
        self.max_health = 100

    def move(self, keys):
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_s] and self.y < HEIGHT:
            self.y += self.speed
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_d] and self.x < WIDTH:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.size, self.size))

    def take_damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)


# ================= ZOMBIE =================
class Zombie:
    def __init__(self, level, boss=False):
        self.boss = boss
        self.size = 20 if not boss else 50
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

        if boss:
            self.speed = 1 + level * 0.3
            self.health = 200 + level * 50
            self.damage = 10 + level * 2
        else:
            self.speed = 1 + level * 0.5
            self.health = 30 + level * 10
            self.damage = 5 + level

    def move_toward(self, player):
        dx = player.x - self.x
        dy = player.y - self.y
        dist = math.hypot(dx, dy)

        if dist != 0:
            self.x += (dx / dist) * self.speed
            self.y += (dy / dist) * self.speed

    def draw(self):
        color = PURPLE if self.boss else DARK_RED
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size))

    def hit(self, damage):
        self.health -= damage


# ================= WEAPON =================
class Weapon:
    def __init__(self):
        self.damage = 25
        self.range = 60
        self.cooldown = 500
        self.last_attack = 0

    def attack(self, player, zombies):
        now = pygame.time.get_ticks()
        if now - self.last_attack < self.cooldown:
            return []

        self.last_attack = now
        hit_zombies = []

        for z in zombies:
            dist = math.hypot(player.x - z.x, player.y - z.y)
            if dist < self.range:
                z.hit(self.damage)
                hit_zombies.append(z)

        return hit_zombies


# ================= GAME =================
class Game:
    def __init__(self):
        self.player = Player()
        self.weapon = Weapon()
        self.zombies = []
        self.level = 1
        self.score = 0
        self.spawn_timer = 0
        self.kills = 0
        self.boss_spawned = False
        self.running = True
        self.powerups = []

    def spawn_zombie(self):
        self.zombies.append(Zombie(self.level))

    def spawn_boss(self):
        self.zombies.append(Zombie(self.level, boss=True))

    def spawn_powerup(self):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        kind = random.choice(["health", "speed", "damage"])
        self.powerups.append([x, y, kind])

    def handle_powerups(self):
        for p in self.powerups[:]:
            px, py, kind = p
            if abs(self.player.x - px) < 20 and abs(self.player.y - py) < 20:
                if kind == "health":
                    self.player.heal(20)
                elif kind == "speed":
                    self.player.speed += 1
                elif kind == "damage":
                    self.weapon.damage += 5
                self.powerups.remove(p)
                self.score += 20

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        # Spawn zombies
        self.spawn_timer += 1
        if self.spawn_timer > 60:
            self.spawn_zombie()
            self.spawn_timer = 0

        # Spawn boss
        if self.kills > 10 * self.level and not self.boss_spawned:
            self.spawn_boss()
            self.boss_spawned = True

        # Move zombies
        for z in self.zombies[:]:
            z.move_toward(self.player)

            # Collision
            if abs(z.x - self.player.x) < 20 and abs(z.y - self.player.y) < 20:
                self.player.take_damage(z.damage)
                self.score -= 5

            # Dead zombie
            if z.health <= 0:
                if z.boss:
                    self.score += 100
                    self.level += 1
                    self.boss_spawned = False
                    self.player.heal(30)
                else:
                    self.score += 10
                    self.kills += 1

                self.zombies.remove(z)

        # Powerups
        if random.randint(1, 200) == 1:
            self.spawn_powerup()

        self.handle_powerups()

    def draw_ui(self):
        health_text = font.render(f"Health: {self.player.health}", True, WHITE)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        level_text = font.render(f"Level: {self.level}", True, WHITE)

        screen.blit(health_text, (10, 10))
        screen.blit(score_text, (10, 40))
        screen.blit(level_text, (10, 70))

    def draw(self):
        screen.fill(BLACK)

        self.player.draw()

        for z in self.zombies:
            z.draw()

        for p in self.powerups:
            color = YELLOW
            pygame.draw.circle(screen, color, (p[0], p[1]), 8)

        self.draw_ui()

        pygame.display.flip()

    def run(self):
        while self.running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        hits = self.weapon.attack(self.player, self.zombies)
                        self.score += len(hits) * 5

            self.update()
            self.draw()

            if self.player.health <= 0:
                self.game_over()

    def game_over(self):
        screen.fill(BLACK)
        text = font.render("GAME OVER - Press R to Restart", True, RED)
        screen.blit(text, (250, 300))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.__init__()
                        waiting = False


# ================= RUN =================
game = Game()
game.run()
pygame.quit()
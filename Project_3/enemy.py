WIDTH = 600
HEIGHT = 800
MAX_BULLETS = 3 
enemies = [] 
def create_enemy():
    for x in range (0,600, 60):
        for y in range (0, 200, 60 ):
            enemy = Actor("enemy", (x,y))
            enemy.vx = level*2
            enemies.append(enemy)

create_enemy()

def move_enemies():
    global score:
    for enemy in enemies:
        enemy.x = enemy.x + enemy.vx
    if enemy.x > WIDTH or enemy.vx < 0:
        enemy.vx = -enemy.vx
        animate(enemy)
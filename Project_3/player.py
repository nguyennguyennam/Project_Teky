WIDTH = 600
HEIGHT = 800
MAX_BULLETS = 3 

def move_player():
    if keyboard.right:
        player.x = player.x + 5
    if keyboard.left:
        player.x = player.x - 5
    if keyboard.up:
        player.y = player.y + 5
    if keyboard.down:
        player.y = player.y - 5
    if player.x > WIDTH:
        player.x = WIDTH
    if player.x < 0:
        player.x = 0
    if player.y > HEIGHT:
        player.y = HEIGHT
    if player.y < 0:
        player.y = 0
    

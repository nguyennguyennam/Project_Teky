import random
import pygame



level = 1
lives = 3
score = 0

background = Actor("background")
player = Actor("player",(200,580))

bullets = []
bombs = []

def draw():
    screen.clear()
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bomb in bombs:
        bomb.draw()
    draw_text()

def update(character):
    move_player()
    move_bullet()
    move_enemies()
    create_bombs()
    move_bombs()
    check_for_end_of_level()

def move_player():
    pass

def move_enemies():
    pass

def  move_bullet():
    pass

def create_bombs():
    pass
def move_bombs():
    pass

def check_for_end_of_level():
    pass


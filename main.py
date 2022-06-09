import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
  # Initialize game and create a screen object.
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")
  # Make an alien.
  alien = Alien(ai_settings, screen)
  ship = Ship(ai_settings, screen)
  # Make a group to store bullets in.
  bullets = Group()
  aliens = Group()
  bg_color = (ai_settings.bg_color)
  gf.create_fleet(ai_settings, screen, ship, aliens)

  while True:
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    gf.update_bullets(bullets)
    gf.update_screen(ai_settings, screen, ship, aliens, bullets)

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
    	if bullet.rect.bottom <= 0:
    		bullets.remove(bullet)
    print(len(bullets))


run_game()
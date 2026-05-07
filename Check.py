import pygame
import time
import pyserial

def check_for_gamepad():
  pyserial.begin(112400)
  pygame.joystick.init()
  try:
    pygame.joystick.Joystick(0).init()
    return(True)
  except:
    return(False)

check = check_for_gamepad()
print(check)
def use_Gamepad():
  if check_for_gamepad() == True:
    pos = Vector2(0.0,0.0)
    pos2 = Vector2(0.0,0.0)
    while true:
      pos.x = pygame.joystick.Joystick(0).get_axis(0)
      pos.y = pygame.joystick.Joystick(0).get_axis(1)
      pos2.x = pygame.joystick.Joystick(0).get_axis(2)
      pos2.y = pygame.joystick.Joystick(0).get_axis(3)
      joined = str(pos) + str(pos2)
      joined.strip("(").strip(")")
      pyserial.send(joined)
      

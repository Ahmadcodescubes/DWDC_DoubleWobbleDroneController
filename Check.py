import pygame
import time
import serial as pyserial
import VectorsPY

def Show_available_ports(OS):
  if OS == "Z":
    return(input("Please enter the COM port of your flight controller (e.g: 'COM4'): "))
  if OS == "X":
    return(input("Please paste the path to your flight controller (e.g: 'dev/TTYusb4'): "))

port_touse = Show_available_ports(input("Enter your OS, Z for windows, X for Linux based OS")) #sets the port_to_use to the user input 

def check_for_gamepad():
  pygame.joystick.init()
  try:
    pygame.joystick.Joystick(0).init()
    return(True)
  except:
    return(False)
  
def Serial_Initialize(porty, Baudratey: int):
  init = pyserial.Serial(porty ,Baudratey)
  return(init)

check = check_for_gamepad()
print(check)
ser = Serial_Initialize(port_touse, 115200)
def use_Gamepad():
  if check == True:
    pos = VectorsPY.Vector2(0.0,0.0)
    pos2 = VectorsPY.Vector2(0.0,0.0)
    while True:
      pos.x = pygame.joystick.Joystick(0).get_axis(0)
      pos.y = pygame.joystick.Joystick(0).get_axis(1)
      pos2.x = pygame.joystick.Joystick(0).get_axis(2)
      pos2.y = pygame.joystick.Joystick(0).get_axis(3)
      joined = str(pos) + str(pos2)
      joined.strip("(").strip(")")
      send_data(joined)
  else:
    print("Connect a controller and restart script to initialize")      

def send_data(data):
    ser.write(data.encode())
    print(f"Sent: {data}")

use_Gamepad()
import pygame
import serial as pyserial
pygame.init()
def Show_available_ports(OS):
  if OS == "Z" or OS == "z":
    return(input("Please enter the COM port of your flight controller (e.g: 'COM4'): "))
  if OS == "X" or OS == "x":
    return(input("Please paste the path to your flight controller (e.g: 'dev/TTYusb4'): "))

port_touse = Show_available_ports(input("Enter your OS, Z for windows, X for Linux based OS: ")) #sets the port_to_use to the user input 

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
    joystick = pygame.joystick.Joystick(0)
    while True:
      pygame.event.pump()
      posx = round(joystick.get_axis(0),1)
      posz = round(joystick.get_axis(1),1)
      pos2rot = round(joystick.get_axis(2),1)
      pos2y = round(joystick.get_axis(3),1)
      joined = str(posx) + str(posz) + str(pos2y) + str(pos2rot)
      joined.strip("(").strip(")")
      send_data(joined)

  else:
    print("Connect a controller and restart script to initialize")      

def send_data(data):
    ser.write(data.encode())
    print(f"Sent: {data}")

send_data("F/C/1")
use_Gamepad()
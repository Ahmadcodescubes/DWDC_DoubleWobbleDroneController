# Example file showing a basic pygame "game loop"
import pygame
import serial
import serial.tools.list_ports
import time

devices = []

for port in serial.tools.list_ports.comports():
    print(f"{port.device}: {port.description}")


def find_device():
    for port in serial.tools.list_ports.comports():
        try:
            ser = serial.Serial(port.device, 115200, timeout=1)
            print(f"Testing {port.device}")
            for i  in range(10):
                ser.write("REPLY".encode("utf-8"))
                time.sleep(0.1)
                readen = ser.readline().decode("utf-8")
                if readen.strip() != "":
                    print(f"Reply from {port.device}: {readen}")
                if readen.strip() == "YES":
                   print(f"{port.device} is the correct port!")
                   ser.close
                   return(port.device)
        except:
           print("Access denied or board not responding")
true_port = find_device()
print(true_port)

# pygame setup
pygame.init()
pygame.font.init()
Tecst = pygame.font.Font()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
my_font = pygame.font.SysFont('Comic Sans MS', 30)

try:
    pygame.joystick.Joystick(0).init()
    tadext = "                               Controller found                           "
    joystick = pygame.joystick.Joystick(0)
except:
    tadext = "Controller not found, connect a controller and restart the script"

text_surface = my_font.render(tadext, True, (255,255,255))
ser = serial.Serial(true_port, 115200, timeout=1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.event.pump()
    posx = round(joystick.get_axis(0),1)
    posz = round(joystick.get_axis(1),1)
    pos2rot = round(joystick.get_axis(3),1)
    pos2y = round(joystick.get_axis(2),1)
    joined = "X: " + str(posx) + " Z: " + str(posz) + " ROT: " + str(pos2y) + " Y: " + str(pos2rot)
    ser.write(joined.encode('utf-8'))
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(text_surface, (200,35))
    screen.blit((my_font.render(joined, True, (255,255,255))), (200, 200))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
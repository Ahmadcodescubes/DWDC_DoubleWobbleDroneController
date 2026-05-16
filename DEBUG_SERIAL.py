import serial
import serial.tools.list_ports
import time

def find_port():
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
                   return(port.device)
        except:
           print("Access denied or board not responding")

correct_port = find_port()
print(f"The correct port is {correct_port}")
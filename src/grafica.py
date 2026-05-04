import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import re
from collections import deque

SERIAL_PORT = 'COM6'
BAUDRATE = 9600
MAX_POINTS = 100

ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)

valores = deque(maxlen=MAX_POINTS)
times = deque(maxlen=MAX_POINTS)
time_counter = 0

regex = re.compile(r"Valor:\s*([0-9.]+)")

def update(frame):
    global time_counter

    line = ser.readline().decode('utf-8').strip()
    print(line)  # 👈 DEBUG: mira qué está llegando

    match = regex.search(line)
    if match:
        valor = float(match.group(1))

        valores.append(valor)
        times.append(time_counter)
        time_counter += 1

        ax.clear()
        ax.plot(times, valores, color='purple') 
        ax.set_ylim(0, 10)
        ax.set_title("Valor Medido")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Valor")
        ax.grid(True)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, interval=1000, cache_frame_data=False)
plt.tight_layout()
plt.show()
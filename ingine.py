import time
import os

os.system('cls' if os.name == 'nt' else 'clear')
p = 45
t = 20
time_1st = time.time()
print("wrr...wrr...wrr...")
time.sleep(3)

while p - ((time.time() - time_1st) * 0.068) > 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nSilnik wlaczony")
    now = time.localtime()
    hours, minutes, seconds = now.tm_hour, now.tm_min, now.tm_sec
    print("|| {:02d}:{:02d}:{:02d} ||".format(hours, minutes, seconds))

    fuel_level = p - ((time.time() - time_1st) * 0.068)
    print("Stan paliwa: {:.3f} l.".format(fuel_level))

    t_o = t + ((time.time() - time_1st) * 0.91)
    if t_o <= 90:
        print("Temperatura oleju: {:.2f} C".format(t_o))
    else:
        print("Temperatura oleju: 90 C")

    t_p = t + ((time.time() - time_1st) * 1.25)
    if t_p <= 115:
        print("Temperatura plynu chlodzacego: {:.2f} C".format(t_p))
    else:
        print("Temperatura plynu chlodzacego: 115 C")

    time.sleep(1)

print("\nBenzyna sie skonczyla! :(\nCzas jazdy: {:.2f}".format(time.time() - time_1st))

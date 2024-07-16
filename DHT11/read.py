import serial
import time
from datetime import datetime

# Accès au port série
PORT = "/dev/ttyACM0"
BAUDRATE = 9600
ser = serial.Serial(PORT, BAUDRATE, timeout=1)

# Attendre que la connexion soit établie
time.sleep(5)

# Temps d'attende entre les lectures du port série
wait_time = 60
with open("output.txt", "w") as file:
    # file.write("temperature;humidity;timespam" + "\n")
    while True:
        try:
            # Lire une ligne de données depuis le port série
            line = ser.readline().decode("utf-8").strip()
            if line:
                date = datetime.now()
                data = line.split(";")
                temp = data[0]
                humi = data[1]

                print(f"temp {temp} | humi {humi} ({date})")

                # Écrire la ligne dans le fichier
                file.write(f"{temp};{humi};{date}" + "\n")

                file.flush()

            time.sleep(wait_time)
        except KeyboardInterrupt:
            print("Programme arrêté par l'utilisateur")
            break
        except Exception:
            pass

ser.close()

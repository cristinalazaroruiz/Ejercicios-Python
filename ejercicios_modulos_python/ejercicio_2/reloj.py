import datetime
import time 
import os 

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        reloj = datetime.datetime.now()
        print(reloj.strftime("%H:%M:%S"))
        time.sleep(1)

except KeyboardInterrupt:
    print("\n Reloj interrumpido")

    




    

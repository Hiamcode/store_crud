import os
import time

def pausa_limpia(segundos=2):
    time.sleep(segundos)
    os.system('cls' if os.name == 'nt' else 'clear')

import requests
import time
from datetime import datetime
from colorama import Fore


"""In this Example, we are going to be spamming the SlothPixel API and checking for the name: Supelion"""
"""You can add a limit if you want to"""

IGN = "supelion"
times = 0
begin = datetime.now()

try:
    while True:
        start = time.time()
        apidata = requests.get(f'https://api.slothpixel.me/api/players/{IGN}').json()
        times += 1
        end = time.time()
        
        if times > 1000:
            print(f"{Fore.RED} Response recieved. Spammed the API {times} time(s). Took: {end - start} seconds. Spamming Since: {begin}")
        elif times > 500:
            print(f"{Fore.YELLOW} Response recieved. Spammed the API {times} time(s). Took: {end - start} seconds. Spamming Since: {begin}")
        else:
            print(f"{Fore.BLUE} Response recieved. Spammed the API {times} time(s). Took: {end - start} seconds. Spamming Since: {begin}")

except Exception as e:
    print(f'Something went wrong! Error: {e}')

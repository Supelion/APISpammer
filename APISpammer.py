import requests
import time
from colorama import Fore
from datetime import datetime

times = 0
begin = datetime.now()

API = input("ENTER API LINK HERE INCLUDING ANY AUTHORIZATIONS SUCH AS AN API KEY: ")


try:
    while True:
        start = time.time()
        apidata = requests.get(API)
        times += 1
        end = time.time()
        
        if times > 1000:
            print(f"{Fore.RED}Response recieved. Spammed the API {times} time(s). Took: {end - start} seconds. Spamming Since: {begin}")
        elif times > 500:
            print(f"{Fore.YELLOW}Response recieved. Spammed the API {times} time(s). Took: {end - start} seconds. Spamming Since: {begin}")
        else:
            print(f"{Fore.BLUE}Response recieved. Spammed the API {times} time(s). Took: {end - start} seconds. Spamming Since: {begin}")

except Exception as e:
    print(f'Something went wrong! Error: {e}')

import time
import os
from datetime import datetime as dt


def host_choice():
    host_unix = '/etc/hosts'
    host_windows = r"C:\Windows\System32\drivers\etc\hosts"
    if os.name in ('nt', 'dos'):
        return host_windows
    elif os.name in ('linux', 'osx', 'posix'):
        return host_unix
    else:
        pass

def hour_comparaison():
    start_hour = dt(dt.now().year,dt.now().month,dt.now().day,8)
    actually_now = dt.now()
    end_hour = dt(dt.now().year,dt.now().month,dt.now().day,16)

    if (start_hour < actually_now) and (actually_now < end_hour):
        return True
    else:
        return False

def main():
    host_redirect = "127.0.0.1"
    website_list = ["www.facebook.com", "facebook.com","https://facebook.com", "www.reddit.com", "reddit.com", "www.9gag.com", 
    "9gag.com", "www.viedemerde.fr","viedemerde.fr", "www.danstonchat.com", "danstonchat.com", 
    "https://danstonchat.com", "https://www.viedemerde.fr"]
    while True:
        if  hour_comparaison():
            with open(host_choice(), 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(host_redirect+" "+website+"\n")
                        
        else:
            with open(host_choice(), 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
        time.sleep(5)

if __name__ == "__main__":
    main()
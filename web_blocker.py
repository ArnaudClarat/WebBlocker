import time
from datetime import datetime as dt


host_unix = '/etc/hosts'
host_windows = r"C:\Windows\System32\drivers\etc\hosts"
host_redirect = "127.0.0.1"
website_list = []

hosts_path = host_unix

def main():
    while True:
        if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(host_redirect+" "+website+"\n")
        else:
            pass
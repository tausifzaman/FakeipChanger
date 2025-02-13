import random
import time
import os

os.system("clear" if os.name == "posix" else "cls")
# Color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

ascii_logo = RED + r'''
  _____ _____      ______/ /                             
 |_   _|  __ \    / ____/ /_  ____ _____  ____  ___  _____
   | | | |__) |  / /   / __ \/ __ `/ __ \/ __ `/ _ \/ ___/
   | | |  ___/  / /___/ / / / /_/ / / / / /_/ /  __/ /    
  _| |_| |      \____/_/ /_/\__,_/_/ /_/\__,_/\___/_/     
 |_____|_|   v1.0.0                          ____/ ''' + RESET


developer_info = YELLOW + '''
Developer : Tausif Zaman
Github    : tausifzaman
instagram : @_tausif_zaman
''' + RESET

def generate_fake_ip():
    """Generate a random fake IP address"""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def main():
    # Print the logo and developer info
    print(ascii_logo)
    print(developer_info)

    # Continuously generate fake IPs
    while True:
        fake_ip = generate_fake_ip()
        print(GREEN + f"[+] Your IP has been changed to {fake_ip}" + RESET)
        time.sleep(0.5)

if __name__ == "__main__":
    main()

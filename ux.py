from downloader import *
from colorama import *
import subprocess

init(autoreset=True)


def li_yue():
    print(Fore.YELLOW + """
    Choose you want to see :  
    [1] Ci Ci
    [2] Xiao
    [3] Hu Tao
    [4] Zhong Li""")

    user_choose = int(input("You choose:  "))
    print("download starting\n")

    if user_choose == 1:
        video = video_downloader("https://youtu.be/_ndVJlqBYLY", "cici")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("cici.mp4", shell=True)
    elif user_choose == 2:
        video = video_downloader("https://youtu.be/sjozpa9DsZU", "xiao")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("xiao.mp4", shell=True)
    elif user_choose == 3:
        video = video_downloader("https://youtu.be/qrH9vMZBwAk", "hutao")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("hutao.mp4", shell=True)
    elif user_choose == 4:
        video = video_downloader("https://youtu.be/4oBpaBEMBIM", "zhongli")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("zhongli.mp4", shell=True)


def mondstat():
    print(Fore.BLUE + """
    Choose you want to see : 
    [1] Fishl
    [2] Mona
    [3] Venti
    [4] Klee\n""")

    user_choose = int(input("You choose:  "))
    print("download starting\n")

    if user_choose == 1:
        video = video_downloader("https://youtu.be/3VtfVPCbNzk", "fishl")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("fishl.mp4", shell=True)
    elif user_choose == 2:
        video = video_downloader("https://youtu.be/QUioSVENXcI", "mona")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("mona.mp4", shell=True)
    elif user_choose == 3:
        video = video_downloader("https://youtu.be/t6BZjmGpq40", "venti")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("venti.mp4", shell=True)
    elif user_choose == 4:
        video = video_downloader("https://youtu.be/C_duDk5e8yU", "klee")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("klee.mp4", shell=True)


def inazuma():
    print(Fore.MAGENTA + """
    Choose you want to see : 
    [1] Kazuha
    [2] Raiden
    [3] Balladeer
    [4] Sara\n""")

    user_choose = int(input("You choose:  "))
    print("download starting\n")

    if user_choose == 1:
        video = video_downloader("https://youtu.be/zif0Lmhrivc", "kazuha")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("kazuha.mp4", shell=True)
    elif user_choose == 2:
        video = video_downloader("https://youtu.be/mvrW4aKwAXw", "raiden")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("raiden.mp4", shell=True)
    elif user_choose == 3:
        video = video_downloader("https://youtu.be/NHEE_-87mNE", "balladeer")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("balladeer.mp4", shell=True)
    elif user_choose == 4:
        video = video_downloader("https://youtu.be/RPAoXtU5Kgg", "sara")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("sara.mp4", shell=True)


def sumeru():
    print(Fore.GREEN + """
        Choose you want to see : 
        [1] Tignari
        [2] Nahida
        [3] Syno
        [4] Dori\n""")

    user_choose = int(input("You choose:  "))
    print("download starting\n")

    if user_choose == 1:
        video = video_downloader("https://youtu.be/oSSCRUmaquo", "tignari")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("tignari.mp4", shell=True)
    elif user_choose == 2:
        video = video_downloader("https://youtu.be/dpZhGzZ3hNc", "nahida")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("nahida.mp4", shell=True)
    elif user_choose == 3:
        video = video_downloader("https://youtu.be/J9WuPBOC_S8", "syno")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("syno.mp4", shell=True)
    elif user_choose == 4:
        video = video_downloader("https://youtu.be/P08q5Y7r9Z4", "dori")
        print(f'"{video}" downloaded successfully!!')
        subprocess.call("dori.mp4", shell=True)

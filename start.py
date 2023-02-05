from ux import *


def start():
    print("Please choose region of personage\n",
    Fore.BLUE + "[1]Mondstat\n",
    Fore.YELLOW + "[2]Li Yue\n",
    Fore.MAGENTA + "[3]Inazuma\n",
    Fore.GREEN + '[4]Sumeru\n')

    user_choose = int(input("You Choose:  "))

    if user_choose == 1:
        mondstat()
    elif user_choose == 2:
        li_yue()
    elif user_choose == 3:
        inazuma()
    elif user_choose == 4:
        sumeru()
    else:
        print("Please, check your choose")


if __name__ == "__main__":
    start()

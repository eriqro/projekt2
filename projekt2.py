import os
from colors import bcolors
import time
list=["eric","cleo","filou"]
def clean():
    os.system('cls')
def plist():
    clean()
    pos=1
    print(bcolors.PURPLE +"Din lista under: ")
    for i in list:
        print(bcolors.CYAN +f"{pos}. {i}")
        pos+=1
def delete(change):
    clean()
    print(bcolors.YELLOW +f"\nNamnet du har valt är:\n{list[change-1]}\n")
    edit=input(bcolors.PURPLE +f"För att ta bort skriv D \nFör att ändra skriv det nya: ").lower()
    if edit=="d":
        print(bcolors.RED +f"\n{list[change-1]} har tagits bort från listan")
        list.pop(change-1)
    else:
        time.sleep(0.5)
        print(bcolors.YELLOW +f"\n{list[change-1]} har ändrats til {edit}")
        list[change-1]=edit       
def add():
    clean()
    list.append(info)
    print(bcolors.GREEN +f"\n{info} har lagts till i listan")  

while True:
    plist()
    info=input(bcolors.GREEN +f"\nVill du ändra/tabort skriv numret till namnet i listan\nEller skriv bara ett namn som borde läggas till: ").lower()
    if info.isdigit():
        delete(int(info))
        time.sleep(2)
    elif info=="n":
        print(bcolors.RED +f"\nHejdå")
        quit()
    else:
        add()
        time.sleep(1)
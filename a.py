import os
import time
from colors import bcolors
def my_function():
    os.system('cls')
    pos=1
    print(bcolors.PURPLE +"Din lista under: ")
    for i in a:
        print(bcolors.CYAN +f"{pos}. {i}")
        pos+=1
    b=input(bcolors.GREEN +f"\nVill du ta bort något i listan ovan j/n?\nEller skriv bara ett namn som borde läggas till: ").lower()
    if b=="j":
        pos=1
        for i in a:
            print(bcolors.CYAN +f"{pos}. {i}")
            pos+=1
        try: 
            tabort=int(input(bcolors.RED +f"\nVilket namn vill du ta bort 1-{len(a)}?: "))
            print(bcolors.RED +f"{a[tabort]} har tagits bort från din lista")
            a.pop(tabort-1)
            time.sleep(1.5)
        except:
            print(bcolors.RED +f"\nAnvänd nummer tack")
    elif b=="n":
        print(bcolors.RED +f"\nHejdå")
        quit()
    else:
        a.append(b)
        print(bcolors.GREEN +f"\n{b} har lagts till i listan")

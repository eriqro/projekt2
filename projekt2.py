import os
os.system('cls')
def my_function():
    print(f"\n{a}")
    b=input(f"\nVill du ta bort något i listan ovan j/n? Eller skriv bara ett namn som borde läggas till: ").lower()
    if b=="j":
        print(a)
        try:
            tabort=int(input(f"\nVilket namn vill du ta bort 1-{len(a)}?: "))
            a.pop(tabort-1)
        except:
            print("\nAnvänd nummer tack")
    elif b=="n":
        print("\nHejdå")
        quit()
    else:
        a.append(b)
        print(f"\n{b} har lagts till i listan")

a=["eric","cleo","filou"]
while True:
    my_function()
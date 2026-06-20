import random
geheim = random.randint(1,100)
tipp = 0
while tipp != geheim:
    tipp = int(input("Errate die Zahl: "))
    if tipp < geheim:
        print("Die Zahl ist zu klein")
    elif tipp > geheim:
        print("Die Zahl ist zu groß")
    else:
        print(f"Du hast die Zahl erraten es war: {geheim}")
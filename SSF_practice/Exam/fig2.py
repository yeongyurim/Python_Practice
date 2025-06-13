weight = float(input("입력: "))
if(weight < 50.8):
    print("Flyweight")
elif(weight < 61.23):
    print("Lightweight")
elif(weight < 72.57):
    print("Middleweight")
elif(weight < 88.45):
    print("Cruiserweight")
else:
    print("Heavyweight")
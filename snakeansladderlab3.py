import random
count=0
while count<=100:
    roll=input("press r to roll a dice")
    if roll=='r':
        r=random.randint(1,6)
        count=count+r
        print("the present value",count)
        print("the dice value",r)
        if(count==8):
            count=37
            print("climb:dice moves to 37")
        elif(count==11):
            count=2
            print("bite:dice moves to 2")
        elif(count==13):
            count=34
            print("climb:dice moves to 34")
        elif(count==25):
            count=4
            print("bite:dice moves to 4")
        elif(count==38):
            count=9
            print("bite:dice moves to 9")
        elif(count==40):
            count=68
            print("climb:dice moves to 68")
        elif(count==52):
            count=81
            print("climb:dice moves to 81")
        elif(count==65):
            count=46
            print("bite:dice moves to 46")
        elif(count==76):
            count=97
            print("climb:dice moves to 97")
        elif(count==89):
            count=70
            print("bite:dice moves to 70")
        elif(count==93):
            count=64
            print("bite:dice moves to 64")
print("You win")


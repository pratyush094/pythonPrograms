def parrot(talking, hour):
    if(talking and (hour<7 or hour>20)):
        print("TRUE")
    else:
        print("FALSE")

parrot(True, 6)
parrot(False, 9)
parrot(True, 5)

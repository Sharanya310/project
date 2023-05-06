import random

ans = input("Do you want to roll a dice y/n")
while ans == 'y':
    no = random.randint(1,6)
    if no ==1:
        print("[------]")
        print("[      ]")
        print("[   0  ]")
        print("[      ]")
        print("[------]")
    elif no==2:
        print("[------]")
        print("[   0  ]")
        print("[      ]")
        print("[   0  ]")
        print("[------]")
    elif no==3:
        print("[------]")
        print("[   0  ]")
        print("[   0  ]")
        print("[   0  ]")
        print("[------]")
    elif no==4:
        print("[------]")
        print("[ 0  0 ]")
        print("[      ]")
        print("[ 0  0 ]")
        print("[------]")
     elif no==5:
        print("[------]")
        print("[ 0  0 ]")
        print("[   0  ]")
        print("[ 0  0 ]")
        print("[------]")
     elif no==6:
        print("[------]")
        print("[ 0  0 ]")
        print("[ 0  0 ]")
        print("[ 0  0 ]")
        print("[------]")   
    ans = print("Enter y/n")
    if ans =='n':
        break
    if ans =='y':
        continue
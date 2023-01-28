'''
Name :Esraa Mohamed 
Project :Rotating_Arrows
'''
import time
import os

while(1):
    os.system('cls')
    for i in range(1,6):
        for j in range(1,6):
            if(j-i==2 or i+j==8 or i==3):
                print("* ",end="")
            else:
                print("  ",end="")
        print()
    print()
    time.sleep(2)
    os.system('cls')
    for j in range(1,6):
        for i in range(1,6):
            if(j-i==2 or i+j==8 or i==3):
                print("* ",end="")
            else:
                print("  ",end="")   
        print()
    print()
    time.sleep(2)
    
    os.system('cls')
    for i in range(1,6):
        for j in range(1,6):
            if(j+i==4 or i-j==2 or i==3):
                print("* ",end="")
            else:
                print("  ",end="")
        print()   
    print()      
    time.sleep(2)
    
    os.system('cls')
    for j in range(1,6):
        for i in range(1,6):
            if(i-j==2 or j+i==4 or i==3):
                print("* ",end="")
            else:
                print("  ",end="")
        print()
    print()     
    time.sleep(2)
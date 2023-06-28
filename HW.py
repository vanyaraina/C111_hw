import random

response = input("Enter y/n: ")

while(response=="y"):
    message = input("Roll the dice")
    number = int(input("Roll the dice to get the face value!  "))
    if number==1:
        print("--------")
        print("        ")
        print("   0    ")
        print("        ")
        print("--------")
    elif(number==2):
        print("--------")
        print("        ")
        print("  0  0  ")
        print("        ")
        print("--------")
    elif(number==3):
        print("--------")
        print("0       ")
        print("   0    ")
        print("      0 ")
        print("--------")
    elif(number==4):
        print("--------")
        print("  0  0  ")
        print("        ")
        print("  0  0  ")
        print("--------")
    elif(number==5):
        print("--------")
        print("  0  0  ")
        print("   0    ")
        print("  0  0  ")
        print("--------")
    elif(number==6):
        print("--------")
        print("  0  0  ")
        print("  0  0  ")
        print("  0  0  ")
        print("--------")
    else:
        print("Choose the corret dice value")


    

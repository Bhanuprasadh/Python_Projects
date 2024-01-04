print("Welcome to the Roller Coaster")
Height = int(input("Enter Your Height - "))
Age = int(input("Enter Your Age - "))

bill = 0


if Height >= 120:
    print("You Can Ride the Roller Coaster")
    if Age<12:
        bill = 250
        print("child tickets are 250 Rupees")
    elif 12<Age<18:
        bill = 350
        print("Youth tickets are 350 Rupees")
    else:
        bill = 500
        print("Adult tickets are 500 Rupees")
        
    wants_photo = input("Do you want to take photo Yes or No")
    if wants_photo == "Yes":
        bill += 50
    
        print(f"Your Final bill is {bill}")
else:
    print("You Can not Ride the Roller Coaster")

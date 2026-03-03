# LOOP practice
# While loop, for loop, range () examples

while True:
    username = input("Enter your username: ")
    if not username:
        print("Username cannot be empty. Please try again.")
    elif len(username) < 8 or len(username) > 15:
        print("Username must be between 8 and 15 characters. Please try again.")
    elif " " in username:
        print("Username cannot contain spaces. Please try again.")
    else:        
        print("Username is valid:", username)
        break

for i in range(3):
    pin = input ("Enter you 4-digit PIN: ")
    if not pin:
        print("PIN cannot be empty. Please try again.")
    elif len(pin)  == 4 and pin.isdigit():
        print("PIN is valid:", pin)
        break   
    elif i == 2:
        print("you have entered an invalid PIN 3 times. Your account is locked.")
        print("please try again after 2minutes.")
    else:
        print("PIN must be 4 digits.")    

      
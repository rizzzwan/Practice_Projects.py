mas_pwd = input("Enter a MASTER password: ")

mode = input("Would you like to add new password or view existing ones? (New/View). Press 'q' to QUIT: ").lower()

# Check if the user wants to quit
if mode == "q": 
    quit()

# Correct condition: check both 'new' and 'view' explicitly
while mode != "new" and mode != "view":
    mode = input("Enter 'NEW' to add and 'VIEW' to view. Press 'q' to QUIT: ").lower()
    
    # Check if the user wants to quit inside the loop
    if mode == "q":
        quit()

# Continue based on the mode
if mode == "new":
    print("Adding new password...")
elif mode == "view":
    print("Viewing passwords...")

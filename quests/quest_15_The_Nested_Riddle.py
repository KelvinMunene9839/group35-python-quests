direction = input("Do you go 'left' or 'right'? ")

if direction == "left":
    action = input("Do you 'swim' or 'wait'? ")
    if action == "swim":
        print("You dive in and find a treasure chest! ")
    else:
        print("You wait... and wait... nothing happens. ")
else:
    print("You head right and find a dead end. ")
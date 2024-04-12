# The Adventure Game: Task 1

while True: # Added for CODE TESTING CONVENIENCE  without needing to leave terminal

# Beginning of Code Correction
    place = input("Choose a place: forest or cave? ") # User Input

    if place == "forest":
        action = input("climb a tree or cross a river?: ") # User Input
        if action == "climb a tree": 
            print("You found a bird's nest!")
        elif action == "cross a river":
            print("You found a boat!")
        else:
            pass # Task 3: Adding pass statement for invalid 

    elif place == "cave": # Setting the Scene: Task 2; expanding the code
        action = input("light a torch or proceed in the dark?: ")
        if action == "light a torch":
           print("Enter the cave.")
        elif action == "proceed in the dark":
             print("Enter with caution! The darkness is full of surprises!")
    else:
        pass # Task 3: Adding pass statement for invalid 
        
  # To continue testing code. NOT REQUIRED FOR ASSIGNMENT!
    choice = input("Do you want to continue? (yes/no): ").lower()

    # If testing is done, end loop. 
    if choice == "no":
        print("Ending the adventure.")
        break  # Exit the loop




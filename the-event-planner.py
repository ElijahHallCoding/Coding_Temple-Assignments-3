# Task 1: Code Correction
while True:  # Loop generated for grading purposes: NOT PART OF ASSIGNMENT

    attendees = int(input("Enter number of attendees: "))  # Convert input to integer 
    venue = "large hall" if attendees > 100 else "conference room"  # Determine venue based on number of attendees 
    print(venue)  # Print the recommended venue 

    facilities = "I recommend using the projector" if attendees < 100 else "I recommend using the audio system"  # Task 2
    print(facilities)  # Print the recommended facilities 

    vegetarian = input("Would you like Vegetarian Caterers?: (yes/no) ") # Task 3

    if vegetarian == "yes":
         print("Veggie Delight Caterers")
    else:
         print("Gourmet Meals Caterers")

    choice = input("Would you like to run the code again? (yes/no): ").lower()  # Run code again for testing/grading? NOT PART OF ASSIGNMENT
    if choice == "no":  # Check if user wants to stop running the code 
         print("Test complete")  # Print message indicating the test is complete 
         break  # Exit the loop if user chooses not to run the code again 
    
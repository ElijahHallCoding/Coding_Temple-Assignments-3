# Task 1: Code Correction
while True:  # Loop generated for grading purposes

    attendees = int(input("Enter number of attendees: "))  # Convert input to integer (1)
    venue = "large hall" if attendees > 100 else "conference room"  # Determine venue based on number of attendees (2)
    print(venue)  # Print the recommended venue (3)

    facilities = "I recommend using the projector" if attendees < 100 else "I recommend using the audio system"  # Determine recommended facilities based on number of attendees (4)
    additional = int(input(facilities))
    print(additional)
    print(facilities)  # Print the recommended facilities (5)

    choice = input("Would you like to run the code again? (yes/no): ").lower()  # Run code again for testing/grading? (6)
    if choice == "no":  # Check if user wants to stop running the code (7)
         print("Test complete")  # Print message indicating the test is complete (8)
         break  # Exit the loop if user chooses not to run the code again (9)
    
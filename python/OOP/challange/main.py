from pet import Pet

def main():
    print("Welcome to Virtual Pet Simulator!")
    pet_name = input("Enter your pet's name: ")
    pet = Pet(pet_name)
    
    # Define available tricks
    tricks = [
        "Sit",
        "Roll Over",
        "Fetch",
        "Play Dead",
        "Shake Hands",
        "Jump"
    ]
    
    while True:
        print("\nMain Menu:")
        print("1. Feed your pet")
        print("2. Play with pet")
        print("3. Put pet to sleep")
        print("4. Train pet")
        print("5. Check status")
        print("6. Show tricks")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            print("\n" + pet.eat())
        elif choice == '2':
            print("\n" + pet.play())
        elif choice == '3':
            print("\n" + pet.sleep())
        if choice == '4':
            print("\nWhich trick would you like to teach?")
            # Display all 6 tricks with proper numbering
            for index, trick in enumerate(tricks, start=1):
                print(f"{index}. {trick}")
                
            while True:
                trick_choice = input("\nEnter the number of the trick (1-6): ")
                if trick_choice.isdigit() and 1 <= int(trick_choice) <= 6:
                    selected_trick = tricks[int(trick_choice)-1]
                    print(f"\n{pet.train(selected_trick)}")
                    break
                else:
                    print("Invalid input! Please enter a number between 1-6.")
        elif choice == '5':
            print(pet.get_status())
        elif choice == '6':
            print("\n" + pet.show_tricks())
        elif choice == '7':
            print(f"\nGoodbye! Take good care of {pet.name}!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1-7.")

if __name__ == "__main__":
    main()
from quiz_data import run_test, view_scores

def show_menu():
    while True:
        print("\nMain Menu:")
        print("1. Start Quiz")
        print("2. View High Scores")
        print("3. Change Subject")
        print("4. Quit")
        choice = input("\nChoose an option (1-4): ").strip()

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid option.")
            continue

        if choice == 1:
            run_test()
        elif choice == 2:
            view_scores()
        elif choice == 3:
            subject_changer()
        elif choice == 4:
            break
        else:
            print("Invalid option.")
        
            

def subject_changer():
    print("\nSubjects Menu:")
    print("1. Math")
    print("2. Science" )
    print("3. Spelling")
    print("4. History")

    while True:
        subject = input("\nChoose an option (1-4): ").strip()

        try:
            subject = int(subject)
        except ValueError:
            print("Invalid option.")
            continue

        if subject == 1:
            return subject
        elif subject == 2:
            return subject
        elif subject == 3:
            return subject
        elif subject == 4:
            return subject     
        else:
            print("Invalid option.")
            continue
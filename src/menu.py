from quiz_data import run_test, view_scores, subject_changer

import os

def show_menu():
    current_test = None
    while True:
        print("\nMain Menu:")
        print("1. Start Quiz (Choose a subject first!)")
        print("2. View High Scores")
        print("3. Choose Subject")
        print("4. Quit")
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            run_test(current_test) if current_test else print("\nChoose a subject first!")
        elif choice == "2":
            view_scores()
        elif choice == "3":
            print("\nSubjects Menu:")
            print("1. Math")
            print("2. Science" )
            print("3. Spelling")
            print("4. History")
            
            subject = input("\nChoose an option (1-4): ").strip()
            current_test = subject_changer(subject)
        elif choice == "4":
            input("\nPress Enter key to continue.")
            break
        else:
            print("Invalid option.")

        input("\nPress Enter key to continue.")

        os.system("clear")
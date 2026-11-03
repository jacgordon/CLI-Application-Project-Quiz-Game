def show_menu():
    print("Javon's Trivia Game!")
    print("\nMain Menu:")
    print("1. Start Quiz")
    print("2. View High Scores")
    print("3. Change Subject")
    print("4. Quit")

    while True:
        subject = input("\nChoose an option 1-4: ").strip()

        try:
            subject = int(subject)
        except ValueError:
            print("Invalid subject.")
            continue

        if subject == 1:
            print("this works!")
            break
        elif subject == 2:
            print("this works!")
            break
        elif subject == 3:
            subject_changer()
            print("\n1. Start Quiz")
            print("2. View High Scores")
            print("3. Change Subject")
            print("4. Quit")
            continue
        elif subject == 4:
            print("\nThank you for playing!")
            break
        else:
            print("Invalid subject.")
            continue
            

def subject_changer():
    print("\nSubjects:")
    print("1. Math")
    print("2. Science" )
    print("3. Spelling")
    print("4. History")

    while True:
        subject = input("\nChoose an option 1-4: ").strip()

        try:
            subject = int(subject)
        except ValueError:
            print("Invalid subject.")
            continue

        if subject == 1:
            print("this works!")
            break
        elif subject == 2:
            print("this works!")
            break
        elif subject == 3:
            print("this works!")
            break
        elif subject == 4:
            print("this works!")
            break     
        else:
            print("Invalid subject.")
            continue
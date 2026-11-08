import datetime

high_scores = []

questions = [
    {"question": "What is 100 + 100?", "choices": "1. 20 \n2. 200\n3. 2000\n4. 1000", "answer": 2},
    {"question": "What is 9 * 6?", "choices": "1. 45  \n2. 63\n3. 54\n4. 56", "answer": 3},
    {"question": "What is 11 * 11?", "choices": "1. 121 \n2. 111\n3. 101\n4. 110", "answer": 1},
    {"question": "What is 119 / 17?", "choices": "1. 6.23 \n2. 7\n3. 9\n4. 8.21", "answer": 2},
    {"question": "What is 73 - 29?", "choices": "1. 46 \n2. 53\n3. 54\n4. 44", "answer": 4},
]

def run_test():
    correct = 0
    answered = 0
    for number, question in enumerate(questions, start=1):
        print(f"Q{number}. {question['question']}")
        print(question["choices"])
        
        while True:
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
            except ValueError:
                print("Invalid option, please try again.\n")
                print(question["question"])
                print(question["choices"])
                continue
            if choice == question["answer"]:
                print("\nCorrect!")
                answered += 1
                correct += 1
                break
            elif choice not in range(1, 5):
                print("Invalid option, please try again.\n")
                print(question["question"])
                print(question["choices"])
                continue
            else:
                print("\nIncorrect.")
                answered += 1
                break
        average = correct / answered * 100
        if number != len(questions):
            print(f"Your current score is {correct}/{answered} {average}%")
        else:
            print("Quiz completed!")
            print(f"Your final score was {correct}/{answered} {average}%")
    if len(high_scores) != 5:
        print("Congratulations! You scored a high score!")
        name = input("Enter your name: ").strip()
        score = {"score": average, "name": name, "date": datetime.date.today().strftime("%m/%d/%y")}
        high_scores.append(score)
                
    


def view_scores():
    if len(high_scores) == 0:
        print("There are no scores yet. Start a quiz!")
        return

    for number, score in enumerate(high_scores, start=1):
        print(f"{number}. {score['score']}% ({score['name']}) {score['date']}")
import datetime

high_scores = []

questions = [
    [
        {"subject": "Math", "question": "What is 100 + 100?", "choices": [20, 200, 2000, 1000], "answer_index": 1},
        {"subject": "Math", "question": "What is 9 * 6?", "choices": [45, 63, 54, 56], "answer_index": 2},
        {"subject": "Math", "question": "What is the square root of 64?", "choices": [8, 4, 16, 32], "answer_index": 0},
        {"subject": "Math", "question": "What is 119 / 17?", "choices": [8, 7, 9, 6], "answer_index": 1},
        {"subject": "Math", "question": "What is 73 - 29?", "choices": [46, 53, 54, 44], "answer_index": 3},
    ],
    [
        {"subject": "Science", "question": "What is the powerhouse of the cell?", "choices": ["Mitochondria", "Nucleus", "Ribosomes", "Cytoplasm"], "answer_index": 0},
        {"subject": "Science", "question": "What is the chemical symbol for the element gold?", "choices": ["Ag", "Fe", "Go", "Au"], "answer_index": 3},
        {"subject": "Science", "question": "What is the largest organ of the human body?", "choices": ["Brain", "Skin", "Liver", "Femur"], "answer_index": 1},
        {"subject": "Science", "question": "At what temperature does water freeze in Celsius?", "choices": ["100 degrees", "-100 degrees", "32 degrees", "0 degrees"], "answer_index": 3},
        {"subject": "Science", "question": "What is the closest planet to the sun?", "choices": ["Venus", "Mars", "Mercury", "Saturn"], "answer_index": 2},
        
    ],
    [
        {"subject": "Spelling", "question": "Which word is spelled correctly?", "choices": ["Acommodation", "Accomodation", "Acomodation", "Accommodation"], "answer_index": 3},
        {"subject": "Spelling", "question": "Which word is spelled correctly?", "choices": ["Separate", "Seperate", "Separete", "Sepperate"], "answer_index": 0},
        {"subject": "Spelling", "question": "Which word is spelled correctly?", "choices": ["Recieve", "Receive", "Riceive", "Reseive"], "answer_index": 1},
        {"subject": "Spelling", "question": "What is the name of the head of a school?", "choices": ["Principal", "Principle", "Princepal", "Principl"], "answer_index": 0},
        {"subject": "Spelling", "question": "Which is the spelling for one thousand years?", "choices": ["Millenium", "Milennium", "Milenium", "Millennium"], "answer_index": 3},
    ],
    [
        {"subject": "History", "question": "Who was the third US president?", "choices": ["Abraham Lincoln", "Thomas Jefferson", "Abraham Lincoln", "George Washington"], "answer_index": 1},
        {"subject": "History", "question": "In which country did the Olympics originate?", "choices": ["Rome", "Egypt", "Greece", "Spain"], "answer_index": 2},
        {"subject": "History", "question": "Which treaty ended war between Germany and the Allied Powers in 1919?", "choices": ["Treaty of Versailles", "Treaty of Germany", "Treaty of Paris", "Treaty of Ghent"], "answer_index": 0},
        {"subject": "History", "question": "In which country did the Industrial Revolution begin?", "choices": ["United States", "France", "Germany", "Great Britain"], "answer_index": 3},
        {"subject": "History", "question": "Which explorer's crew completed the first sail around the entire world?", "choices": ["Marco Polo", "Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan"], "answer_index": 3},
    ]
]


def run_test(test):
    correct = 0
    answered = 0

    for number, question in enumerate(questions[test - 1], start=1):
        while True:
            print(f"Q{number}. {question['question']}")
            for i in range(4):
                print(f"{i + 1}) {question["choices"][i]}")
            
            try:
                choice = int(input("Enter your choice (1-4): ").strip()) - 1
            except ValueError:
                print("Invalid option, please try again.\n")
                continue
            
            if choice == question["answer_index"]:
                print("\nCorrect!")
                answered += 1
                correct += 1
                break
            elif choice not in range(4):
                print("Invalid option, please try again.\n")
                continue
            else:
                print("\nIncorrect.")
                answered += 1
                break
        
        average = correct / answered * 100
        if number != len(questions[test - 1]):
            print(f"Your current score is {correct}/{answered} {average:.2f}%")
        else:
            print("Quiz completed!")
            print(f"Your final score was {correct}/{answered} {average:.2f}%")
    
    if len(high_scores) != 5:
        print("Congratulations! You scored a high score!")
        name = input("Enter your name: ").strip()
        score = {"subject": questions[test - 1][0]["subject"], "score": average, "name": name, "date": datetime.date.today().strftime("%m/%d/%y")}
        high_scores.append(score)
    
    if len(high_scores) == 5 and average > high_scores[-1]["score"]:
        high_scores.pop()
        print("Congratulations! You scored a high score!")
        name = input("Enter your name: ").strip()
        score = {"subject": questions[test - 1][0]["subject"], "score": average, "name": name, "date": datetime.date.today().strftime("%m/%d/%y")}
        high_scores.append(score)

    high_scores.sort(key=get_score, reverse=True)
                

def view_scores():
    if len(high_scores) == 0:
        print("\nThere are no scores yet. Start a quiz!")
        return

    print("High scores:")
    for number, score in enumerate(high_scores, start=1):
        print(f"{number}. {score['subject']} {score['score']}% ({score['name']}) {score['date']}")


def get_score(score):
    return score["score"]


def subject_changer(subject):
    while True:
        if subject == "1":
            return int(subject)
        elif subject == "2":
            return int(subject)
        elif subject == "3":
            return int(subject)
        elif subject == "4":
            return int(subject)     
        else:
            print("Invalid option.")
            break
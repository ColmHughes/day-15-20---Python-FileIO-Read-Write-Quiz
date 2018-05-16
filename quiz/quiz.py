def show_menu():
    print("1. Ask Questions")
    print("2. Add a Question")
    print("3. Exit")

    return input("Enter your choice: ")

def ask_questions():
    with open("questions.txt", "r") as f:
        lines = f.read().split('\n')
        
    numbered_lines = list(enumerate(lines))
    questions = [t for n, t in numbered_lines if n % 2 == 0]
    answers = [t for n, t in numbered_lines if n % 2 != 0]
    q_and_a = list(zip(questions, answers))
    
    for q, a in q_and_a:
        guess = input(q)
        if guess == a:
            print("Correct!!!")
        else:
            print("Looooser!!!")
    
    for n, t in numbered_lines:
        if n % 2 == 0:
            questions.append(t)
        else:
            questions.append(t)

def add_a_question():
    question = input("Enter a question: ")
    answer = input("OK, tell me the answer: ")
    with open("questions.txt", "a") as f:
        f.write("\n" + question)
        f.write("\n" + answer)
    
def game_loop():
    while True:
        option = show_menu()
        
        if option == "1":
            ask_questions()
            
        if option == "2":
            add_a_question()        
            
        if option == "3":
            print("ok bye")
            break
        
game_loop()
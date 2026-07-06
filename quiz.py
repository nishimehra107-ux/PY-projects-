questions=("what is the capital of india?",
           "which festival is the festival of lights?",
           "who is the king of jungle?",
           "how many bones are there in human body?")


options = (("A.Goa","B.New Delhi","C.Indore","D.Gwalior"),
           ("A.Diwali","B.Holi","C.Eid","D.New Year"),
           ("A.Rabbit","B.Kuala","C.Lion","D.Elephant"),
           ("A.206","B.207","C.209","D.210"))

answers =("B" , "A" , "C" , "A" )
guesses=[]
score=0
question_num=0

for question in questions:
    print("----------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1

print("--------------------")
print("      RESULTS       ")
print("--------------------")

print("answers: ",end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess, end="")
print()

score= score/len(questions)*100 
print(f"your score is : {score} % ")
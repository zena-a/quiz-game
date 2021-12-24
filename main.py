# Quiz Game
# Built with basic OOP concepts
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# An empty list
question_bank = []

# Loops through question_data
# Creates a Question object that receives values 'question' and 'answer'
# Stores the Question object into the question_bank list
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Creates a QuizBrain object, that takes a list of questions
quiz = QuizBrain(question_bank)

# Loops through the list of questions until all are answered
while quiz.still_has_questions():
    quiz.next_question()

# Prints player's final score
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

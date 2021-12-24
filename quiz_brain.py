class QuizBrain:
    """
        A class used to represent the quiz logic
        ...
        Attributes
        ----------
        question_number : int
            The number of the current question
        question_list : list
            The list of questions for the quiz
        score : int
            The total score of correct answers from the user

        Methods
        -------
        still_has_questions(self)
            Returns true if there are more questions in the quiz
        next_question(self)
            Selects and prints questions from list and checks user's answer
        check_answer(user_answer, correct_answer)
            Checks and prints if user got the answer right or wrong
        """
    # Constructor
    def __init__(self, q_list):
        """
        Parameters
        ----------
        q_list : list
            The list of questions for the quiz
        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Returns true if there are more questions in the quiz."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Selects and prints questions from list and checks user's answer."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks and prints if user got the answer right or wrong.

        If user answer is correct, it updates the score by 1.
        Prints user's current score throughout game.

        Parameters
        ----------
        user_answer : str
            The user's answer to the current question
        correct_answer : str
            The correct answer to the current question

        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

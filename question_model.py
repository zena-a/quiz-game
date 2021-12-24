class Question:
    """
    A class used to represent a quiz question along with its answer
    ...
    Attributes
    ----------
    text : str
        The question
    answer : str
        The correct answer to the question
    """
    # Constructor
    def __init__(self, q_text, q_answer):
        """
        Parameters
        ----------
        q_text : str
            The question
        q_answer : str
            The correct answer to the question
        """

        self.text = q_text
        self.answer = q_answer

'''
Module represents mechanism that run the whole app
'''

from datetime import datetime

class Quiz:
    '''
    Class that represents quiz mechanism and service user.
    '''

    def __init__(self, data: list) -> None:

        """
        The __init__ function is the first function that gets called
        when you create a new instance of a class.
        It's job is to initialize all of the attributes for an object.
        In this case, we are initializing two attributes: data and app.

        :param self: Represent the instance of the class
        :param data: list: Pass in a list of data to the class
        :return: None
        :doc-author: Trelent
        """
        self.data = data
        self.app()
        self.pass_record()

    def app(self):
        '''
        Screen for user, displays questions with answers. Sum score

        :return: score - properly answered questions
        '''
        answers_list = ['A', 'B', 'C', 'D']
        self.score = 0

        self.user_name = input('Enter you username: ')
        print('Chose you answer by pressing A,B,C or D to set your choice')
        for index, position in enumerate(self.data, start=1):
            print(f'Question {index}: {position["question"]}')
            for option, answer in zip(answers_list, position['answers']):
                print(f'{option} - {answer}')
            user_answer = input('Whats your answer?: ')
            try:
                while True:
                    if user_answer.upper() not in answers_list:
                        raise ValueError('Incorrect type. Try again')

                    print(f'Your answer is {user_answer.upper()}')
                    if user_answer.lower() in position['right answer']:
                        self.score += 1
                    break
            except ValueError as e:
                print(e)

        print(f'You score is: {self.score}')
        return self.score

    def user_answer(self):

        """
        The user_answer function takes the user's input and returns it in upper case.

        :param self: Refer to the object itself
        :return: The user's answer
        :doc-author: Trelent
        """
        user_answer = input("Whats's your answer?: ")
        return user_answer.upper()

    def pass_record(self) -> dict:
        """
        The pass_record function takes the user's name and score, as well as the current time,
        and returns a dictionary containing all of this information.

        :param self: Access the attributes of the class
        :return: A dictionary with the user name, score and time
        :doc-author: Trelent
        """
        record = {}
        record.update({'name': self.user_name,
                       'score': self.score,
                       'time': datetime.now().strftime('%Y-%m-%d %H:%M')})
        return record
    # def check_answer(self, user_answer, right_answer):
    #     pass

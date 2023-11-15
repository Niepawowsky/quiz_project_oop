from datetime import datetime


class Quiz:
    def __init__(self, data: list) -> None:
        self.data = data
        self.app()
        self.pass_record()


    def app(self):
        '''
        Screen for user, displays questions with answers. Sum score
        :return:
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
                    else:
                        print(f'Your answer is {user_answer.upper()}')
                        if user_answer.lower() in position['right answer']:
                            self.score += 1
                        break
            except ValueError as e:
                print(e)

        print(f'You score is: {self.score}')
        return self.score

    def user_answer(self):
        user_answer = input("Whats's your answer?: ")
        return user_answer.upper()

    def pass_record(self) -> dict:
        record = {}
        record.update({'name' : self.user_name,
                      'score': self.score,
                      'time' : datetime.now().strftime('%Y-%m-%d %H:%M')})
        return record
    # def check_answer(self, user_answer, right_answer):
    #     pass

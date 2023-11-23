import json
from quiz.quiz import Quiz
from scoreboard.scoreboard import Scoreboard, ScoreboardViewer

if __name__ == '__main__':
    chose = input("For quiz play press - 1, for scoreboard view press 2: ")

    if chose == '1':
        with open('quiz/questions.json', mode='r', encoding='UTF8') as file:
            data = json.load(file)

            quiz_instance = Quiz(data)

            record = quiz_instance.pass_record()
            Scoreboard(record)
    elif chose == '2':
        viewer = ScoreboardViewer()

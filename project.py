from tabulate import tabulate
import requests
import html


class Questions:
    topics = [
        ["A", "General Knowledge"],
        ["B", "History"],
        ["C", "Mathematics"],
        ["D", "Geography"],
        ["E", "Mythology"],
        ["F", "Politics"],
        ["G", "Art"],
        ["H", "Vehicles"],
        ["I", "Sports"],
    ]
    ids = {
        "a": "9",
        "b": "23",
        "c": "19",
        "d": "22",
        "e": "20",
        "f": "24",
        "g": "25",
        "h": "28",
        "i": "21",
    }

    def __init__(self):
        print("Grades")
        print(
            f"{tabulate([["8-10", "Excellent"], ["6-7", "Good"], ["4-5", "Average"], ["0-3", "Low"]],
                          headers=["Score", "Grade"], tablefmt="grid")}\n"
        )

        self.category = self.check_options()
        self.question_count = 10
        self.questions_data = self.get_questions()

    @classmethod
    def check_options(cls):
        print("Topics")
        print(
            tabulate(cls.topics, headers=["OPTIONS", "CHOICE"], tablefmt="simple_grid")
        )
        while True:
            choice = input(
                "Choose An Option From Table, e.g..'A' For General Knowledge: "
            ).capitalize()
            if choice.lower() in cls.ids:
                return cls.ids[choice.lower()]
            # In case user gave wrong option, it tells them and redos
            print("Wrong Option, Please Choose From Table")

    def get_questions(self):  # API to get the questions
        response = requests.get(
            f"https://opentdb.com/api.php?amount={self.question_count}&category={self.category}&type=boolean"
        )
        question_data = []

        for n in response.json()["results"]:
            question_info = html.unescape(n["question"]), html.unescape(
                n["correct_answer"]
            )
            question_data.append(question_info)
        return question_data


def main():
    print("Welcome to TriviQ - Trivia Quiz")  # Project Name
    questions = Questions()
    score = question_data(questions.questions_data)
    grade = check_grade(score)
    print(f"\nYour Grade is {grade} with a score of {score}/10")


def question_data(
    infos, users_answers=None
):  # handles questions and answers from the API
    score = 0
    for no in range(len(infos)):
        question_info = infos[no]
        question, answer = question_info

        # I did this conditional block for pytests
        if users_answers != None:  # this passes an users_input to allow pytest testing
            users_input = users_answers[no]
            score += validate_answer(no, question, answer, users_input=users_input)
        else:  # this would leave the users_input as None
            score += validate_answer(no, question, answer)

    return score


def validate_answer(
    n, question, answer, users_input=None
):  # checks for right/wrong answers
    while True:
        if users_input != None:  # acepts a users_input for my pytest
            users_answer = users_input
        else:
            users_answer = input(
                f"\n{n + 1}). {question} Enter Answer(True/False): "
            ).strip()

        # if users doesn't give true or false
        if users_answer.lower() not in ["true", "false"]:
            print("Please choose True/False")
            if users_input != None:
                # i did this for my pytest, if users input is not true/false we wont fall into a loop
                return None
            continue  # restarts loop

        if users_answer.lower() == answer.lower():
            print("correct! ✅")
            return 1  # return 1 point and breaks loop
        else:
            print("wrong! ❌")
            return 0  # returns 0 point and breaks loop


def check_grade(score):  # for grading the score
    if int(score) >= 8:
        return "Excellent"
    if int(score) >= 6:
        return "Good"
    if int(score) >= 4:
        return "Average"
    return "Low"


if __name__ == "__main__":
    main()

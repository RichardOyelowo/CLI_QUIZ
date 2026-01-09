from project import question_data
from project import validate_answer
from project import check_grade


def test_question_data():
    info = [
        ("My name is Richard", "True"),
        ("I hate CS50", "False"),
        ("I love programming", "True"),
    ]
    users_input = ["True", "True", "True"]
    
    assert question_data(infos=info,users_answers=users_input) == 2


def test_validate_answer():
    question = "My name is Richard"

    assert validate_answer(0, question=question, answer="True", users_input="True") == 1
    assert validate_answer(0, question=question, answer="True", users_input="true") == 1
    assert validate_answer(0, question=question, answer="True", users_input="False") == 0


# not testing for alpha char because my project structure handles such earlier
def test_check_grade():
    assert check_grade(10) == "Excellent"
    assert check_grade(9) == "Excellent"
    assert check_grade(7) == "Good"
    assert check_grade(5) == "Average"
    assert check_grade(3) == "Low"

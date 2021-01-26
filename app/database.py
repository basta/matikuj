from .models import Problem
from typing import List

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField, FileField
from wtforms.validators import DataRequired

data: List[Problem] = []

def get_problem_form(problem: Problem):
    """
    Returns a form to be displayed on a question page.
    Not implemented yet.
    """
    return


def update_data() -> None:
    """
    Loads a problems from database into data.
    Now just a mere mock.
    """
    data = [
            Problem(
                typ="field",
                body="Whizzmot je ...?",
                difficulty=1,
                tags="životně důležité otázky, whizzmot",
                result="nejlepší",
                submitter=1
                ),
            Problem(
                typ="field",
                body="Višta je ...?",
                difficulty=3,
                tags="životně důležité otázky",
                result="nejlepší",
                submitter=1
                )
            ]

update_data()

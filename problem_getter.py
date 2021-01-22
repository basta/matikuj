from import db
from models import Problem

def get_all_problems():
    return Quiz.Problem.all()
    

def get_quizes_by_difficulty(diff: int):
    return Quiz.Problem.filter_by(difficulty=diff).all()


def get_quizes_by_type(typ: str):
    return Quiz.Problem.filter_by(typ=typ).all()


def get_quizes_by_tags():
    raise NotImplementedError

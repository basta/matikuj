from import db
from models import Quiz

def get_all_quizes():
    return Quiz.query.all()
    

def get_quizes_by_difficulty(diff: int):
    return Quiz.query.filter_by(difficulty=diff).all()


def get_quizes_by_type(typ: str):
    return Quiz.query.filter_by(typ=typ).all()

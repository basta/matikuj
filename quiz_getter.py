from import db
from models import Quiz

def all():
    return Quiz.query.all()
    

def by_difficulty(diff: int):
    return Quiz.query.filter_by(difficulty=diff).all()


def by_type(typ: str):
    return Quiz.query.filter_by(typ=typ).all()


def ordered_by_views():
    return Quiz.query.order_by(Quiz.views).all()

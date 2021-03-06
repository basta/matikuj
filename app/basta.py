import random
import string
from typing import List
from app import app, db
from .models import *

def quiz_selection() -> List[int]:
    pass

class Member:
    def __init__(self, member_id:str, current_session_id:str):
        self.member_id = member_id
        self.current_session_id = current_session_id
        self.name = Member.random_id()

    @staticmethod
    def random_id() -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


class Session:
    def __init__(self, session_id: str):
        self.members: List[Member] = []
        self.id = session_id
    
    def add_member(self, member: Member):
        self.members.append(member)

    @staticmethod
    def random_id() -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

import random
import string
from typing import List

class Session:
    def __init__(self, session_id: str):
        self.members: List[Member] = []
        self.id = session_id
    
    @staticmethod
    def random_id() -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

class Member:
    def __init__(self, member_id:str, current_session_id:str):
        self.member_id = member_id
        self.current_session_id = current_session_id

    @staticmethod
    def random_id() -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

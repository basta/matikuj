class Session:
    def __init__(self, session_id: str):
        self.members = []
        self.id = session_id

class Member:
    def __init__(self, member_id:str, current_session_id:str):
        self.member_id = member_id
        self.current_session_id = current_session_id


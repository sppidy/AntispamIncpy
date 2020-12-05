from enum import Enum, auto
from typing import Optional

class ClassTypes:
    def __str__(self) -> str:
        return f'<{self.__class__.__name__}: {self.__dict__}>'

    def __repr__(self) -> str:
        return self.__str__()

class Antispamclass(ClassTypes):
    token: str
    userid: int
    reason: str
    def __init__(self, reason: str, token: str, userid: int, **kwargs) -> None:
        self.token = token
        self.userid = userid
        self.reason = reason

from dataclasses import dataclass

from logic.exeption.base import LogicException

@dataclass(eq=False)
class ChatWithThatTitleAlreadyExistsException(LogicException):
    title: str
    
    @property
    def message(self):
        return f'Чат с таким названием "{self.title}"уже существует'
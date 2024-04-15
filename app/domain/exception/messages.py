from dataclasses import dataclass

from domain.exception.base import AplicationException

@dataclass(eq=False)
class TitleTooLongException(AplicationException):
    text: str
    
    @property
    def message(self):
        return f'Текст "{self.text}" слишком длинный'
    
@dataclass(eq=False)
class EmptyTextException(AplicationException):
    @property
    def message(self):
        return f'Текст не может быть пустым'
from dataclasses import dataclass

from domain.exception.base import AplicationException

@dataclass(eq=False)
class TextTooLongError(AplicationException):
    text: str
    
    @property
    def message(self):
        return f'Текст "{self.text}" слишком длинный'
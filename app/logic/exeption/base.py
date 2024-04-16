from dataclasses import dataclass

from domain.exception.base import AplicationException

@dataclass(eq=False)
class LogicException(AplicationException):
    
    @property
    def message(self):
        return f'В обработке запроса возникла ошибка'
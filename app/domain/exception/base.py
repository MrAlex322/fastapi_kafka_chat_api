from dataclasses import dataclass

@dataclass(eq=False)
class AplicationException(Exception):
    @property
    def message(self):
        return 'Произошла ошибка приложения'

from dataclasses import dataclass

from logic.exeption.base import LogicException

@dataclass(eq=False)
class  EventHandlersNotRegisteredException(LogicException):
    event_type = str
    @property
    def message(self):
        return f'Не удалось найти обработчики для события: {self.event_type}'

@dataclass(eq=False)
class CommandHandlersNotRegisteredException(LogicException):
    command_type = str
    @property
    def message(self):
        return f'Не удалось найти обработчики для команд: {self.command_type}'
    
from dataclasses import dataclass

from domain.values.base import BaseValueObject
from domain.exception.messages import EmptyTextException, TitleTooLongException

@dataclass(frozen=True)
class Text(BaseValueObject):
    value = str
    def validate(self):
        if not self.value:
            raise EmptyTextException(self.value)
        
    def as_generic_type(self) -> str:
        return str(self.value)

@dataclass(frozen=True)
class Title(BaseValueObject):
    value = str 
    def validate(self):
        if not self.value:
            raise EmptyTextException(self.value)       
        if len(self.value) > 255:
            raise TitleTooLongException(self.value)
        
    def as_generic_type(self):
        return str(self.value)
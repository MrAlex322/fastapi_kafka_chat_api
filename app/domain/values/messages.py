from dataclasses import dataclass

from domain.values.base import BaseValueObject
from domain.exception.messages import TextTooLongError

@dataclass(frozen=True)
class Text(BaseValueObject):
    value = str 
    def validate(self):
        if len(self.value) > 255:
            raise TextTooLongError(self.value)
        
    def as_generic_type(self):
        return str(self.value)
from typing import TypeVar

import pydantic

__all__ = ["Command", "BaseCommand"]

BaseCommand = TypeVar("BaseCommand", bound="Command")


class Command(pydantic.BaseModel):
    ...

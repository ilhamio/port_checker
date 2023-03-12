from pydantic import PositiveInt

from application.pkg.entities.base.command import Command

__all__ = [
    "StartCommand"
]


class StartCommand(Command):
    timeout: PositiveInt
    file: str
    result: str

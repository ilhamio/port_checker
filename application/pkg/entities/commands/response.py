from application.pkg.entities.base import Command

__all__ = ["StartUseCaseResponseCommand"]


class StartUseCaseResponseCommand(Command):
    status: bool
    message: str

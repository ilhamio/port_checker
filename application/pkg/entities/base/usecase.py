import abc
from typing import Any, TypeVar
from application.pkg.entities.base.command import Command

__all__ = ["UseCase", "BaseUseCase"]

BaseUseCase = TypeVar("BaseUseCase", bound="UseCase")


class UseCase(abc.ABC):
    """
    Base abstract UseCase class.

    UseCase pattern is used for delegate business logic from presentation layer
    to domain.
    Example:

    class CheckUserPermissionUseCase(UseCase):
        user_service: Service

        def __init__(service: Service):
            self.user_service = service

        def execute(cmd: Model) -> bool:
            data = validate_date(cmd)
            has_perm = self.user_service.check_perm(data)
            if not has_perm:
                raise AccessDeniedException
            ....
            return True
    """

    def execute(self, cmd: Command | None) -> Any:
        """
        Entrypoint of UseCase class
        :param cmd: Instance of base command class.
        """
        raise NotImplementedError

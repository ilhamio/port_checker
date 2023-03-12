import asyncio
from typing import List

from application.domain.services import get_csv_data, save_data_to_csv
from application.pkg.entities.base import UseCase
from application.pkg.entities.commands import StartCommand, CSVRowCommand, StartUseCaseResponseCommand
from application.pkg.entities.exceptions.csv import NoSuchFileOrDirectoryException
from application.pkg.entities.exceptions.host import ClientConnectionException
from application.pkg.handlers.command import COMMAND_HANDLERS


class StartUseCase(UseCase):
    """
    UseCase for starting main operation
    """

    async def execute(self, cmd: StartCommand) -> StartUseCaseResponseCommand:
        try:
            csv_data: List[CSVRowCommand] = await get_csv_data(cmd.file)
        except NoSuchFileOrDirectoryException:
            return StartUseCaseResponseCommand(status=False, message="Не существует исходного файла!")

        try:
            data = await asyncio.gather(*[COMMAND_HANDLERS.get(type(host))(host, timeout=cmd.timeout) for host in csv_data])
        except ClientConnectionException:
            return StartUseCaseResponseCommand(status=False,
                                               message="Проблемы с интернет соединением на стороне клиента!")
        data = list(filter(lambda x: True if x else False, data))
        await save_data_to_csv(cmd.result, data)
        return StartUseCaseResponseCommand(
            status=True,
            message=f"Операция успешно выполнена! Результат ожидает вас в файле {cmd.result}"
        )

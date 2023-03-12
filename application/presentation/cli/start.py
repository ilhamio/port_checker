"""
CLI module stores cli groups and commands

CLI command must have arguments WITH ANNOTATION (!!!):
    cmd - command which extend BaseCommand ABC
    usecase - class with business logic
"""
import asyncio

import click

from application.pkg.entities.base import BaseUseCase
from application.pkg.entities.commands import StartCommand, StartUseCaseResponseCommand
from application.pkg.settings import RESULT_FILE_NAME, HOST_WAIT_TIMEOUT
from application.presentation.utils.di import inject


@click.command()
@click.option('--timeout', default=HOST_WAIT_TIMEOUT,
              help='Total duration in seconds to wait response while check port openning.')
@click.option('--file', prompt='file name in /files/ directory', help='Path to CSV files directory.')
@click.option('--result', default=RESULT_FILE_NAME, help='Result file name.')
@inject
async def start(cmd: StartCommand, usecase: BaseUseCase) -> None:
    result: StartUseCaseResponseCommand = await usecase.execute(cmd=cmd)
    if result.status:
        print(result.message)
    else:
        print("Произошла ошибка: ", result.message)


@click.group()
def cli():
    """
    Main command group
    """
    pass


cli.add_command(start, name='start')

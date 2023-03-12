from application.domain import usecases
from application.pkg.entities import commands

EVENT_HANDLERS = {
    commands.StartCommand: usecases.StartUseCase
}

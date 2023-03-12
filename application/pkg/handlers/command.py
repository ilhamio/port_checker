from application.domain.services import ping_host, wait_host_port, nothing
from application.pkg.entities import commands

COMMAND_HANDLERS = {
    commands.PingCommand: ping_host,
    commands.FullRowCommand: wait_host_port,
    commands.NotValidRowCommand: nothing
}

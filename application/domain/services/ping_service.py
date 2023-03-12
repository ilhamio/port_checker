import datetime
from typing import List

import pythonping

from application.pkg.entities import commands
from application.pkg.settings import HOST_WAIT_TIMEOUT, PING_COUNT

__all__ = ['ping_host']


async def ping_host(
        cmd: commands.PingCommand,
        count: int = PING_COUNT,
        timeout: int = HOST_WAIT_TIMEOUT
) -> List[commands.CSVResultCommand]:
    """
    Function for pinging remote server
    :param cmd: row from csv file
    :param count: attempts count
    :param timeout: timeout in seconds
    :return:
    """
    data = []
    for ip in cmd.ips:
        data.append(
            commands.CSVResultCommand(
                timestamp=datetime.datetime.now(),
                domain=cmd.domain,
                ip=ip,
                rtt=round(pythonping.ping(ip, count=count, timeout=timeout).rtt_avg * 1000)
            )
        )
    return data

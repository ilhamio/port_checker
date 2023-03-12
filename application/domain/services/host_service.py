import asyncio
import datetime
import time
from typing import List

from application.pkg.entities import commands
from application.pkg.entities.exceptions.host import ClientConnectionException
from application.pkg.settings import HOST_WAIT_TIMEOUT, PORT_STATUS

__all__ = ['wait_host_port']


async def wait_host_port(
        cmd: commands.FullRowCommand,
        timeout: int = HOST_WAIT_TIMEOUT
) -> List[commands.CSVResultCommand]:
    """Repeatedly try if a port on a host is open until duration seconds passed

    Returns
    -------
    List of CSVResultCommand
    """
    data = []
    for ip in cmd.ips:
        for port in cmd.ports:
            try:
                t = time.time()
                _, writer = await asyncio.wait_for(asyncio.open_connection(ip, port), timeout=timeout)
                rtt = time.time() - t
                writer.close()
                await writer.wait_closed()
                data.append(
                    commands.CSVResultCommand(
                        timestamp=datetime.datetime.now(),
                        domain=cmd.domain,
                        ip=ip,
                        port=port,
                        status=PORT_STATUS[True], rtt=round(rtt * 1000, 2))
                )
            except OSError:
                raise ClientConnectionException
            except Exception as e:
                print(e)
                data.append(
                    commands.CSVResultCommand(
                        timestamp=datetime.datetime.now(),
                        domain=cmd.domain,
                        ip=ip,
                        port=port,
                        status=PORT_STATUS[False],
                        rtt=timeout * 1000)
                )

    return data

import datetime
from typing import List

from pydantic import validator
from decimal import Decimal

from application.pkg.entities.base import Command

__all__ = [
    "CSVRowCommand",
    "FullRowCommand",
    "NotValidRowCommand",
    "PingCommand",
    "CSVResultCommand"
]


class CSVRowCommand(Command):
    pass


class FullRowCommand(CSVRowCommand):
    domain: str | None
    ports: List
    ips: List[str]


class NotValidRowCommand(CSVRowCommand):
    domain: str | None
    ports: List[int | None] | None


class PingCommand(CSVRowCommand):
    domain: str | None
    ips: List[str]


class NotValidDomainCommand(CSVRowCommand):
    domain: str
    ports: List | None


class CSVResultCommand(Command):
    timestamp: datetime.datetime
    domain: str = "???"
    ip: str
    rtt: Decimal
    port: int = -1
    status: str = "???"

    @validator('domain')
    def default_str(cls, v):
        if v is None:
            return "???"
        return v

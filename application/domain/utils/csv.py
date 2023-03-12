import csv
import re

from application.pkg.settings import CSV_DELIMITER

IP_V4 = "^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"  # noqa
DOMAIN = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"





def check_ipv4(data: str) -> bool:
    return re.match(IP_V4, data) is not None


def check_domain(data: str) -> bool:
    return re.match(DOMAIN, data) is not None


def get_host_type(host: str) -> str | None:
    if check_ipv4(host):
        return 'ipv4'
    elif check_domain(host):
        return 'domain'
    elif host == 'localhost':
        return 'localhost'
    return None


def validate_filename(filename: str):
    if filename.endswith('.csv'):
        return filename
    return filename + '.csv'

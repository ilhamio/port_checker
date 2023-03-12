import csv
from typing import List

from application.domain.services.resolve_domain_service import resolve_domain
from application.domain.utils.csv import get_host_type, validate_filename
from application.pkg.entities.commands import NotValidRowCommand, PingCommand, FullRowCommand, CSVResultCommand
from application.pkg.entities.exceptions.csv import NoSuchFileOrDirectoryException
from application.pkg.settings import CSV_LIST_DELIMITER, CSV_DELIMITER, CSV_SAVE_NEWLINE, FILES_DIRECTORY

__all__ = ['get_csv_data', 'save_data_to_csv']


async def save_data_to_csv(
        filename: str,
        data: List[List[CSVResultCommand]],
        delimiter: str = CSV_DELIMITER,
        newline: str = CSV_SAVE_NEWLINE
):
    """
    Save to csv file function
    :param filename: file in directory
    :param data: data for saving
    :param delimiter: delimiter for saving csv
    :param newline: newline for saving csv
    :return:
    """
    file_directory = FILES_DIRECTORY + validate_filename(filename)
    with open(file_directory, 'w', newline=newline) as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter, quotechar='|')
        writer.writerow(['Timestamp', 'Domain', 'IP', 'RTT', 'Port', 'Status'])
        for i in data:
            for j in i:
                writer.writerow([j.timestamp, j.domain, j.ip, j.rtt, j.port, j.status])


async def get_csv_data(
        filename: str,
        csv_list_delimiter: str = CSV_LIST_DELIMITER
) -> List:
    """
    Get data from csv file
    :param filename: path to file with file
    :param csv_list_delimiter: delimiter in csv row
    :return:
    """
    try:
        data_from_csv = read_csv_data(filename)
    except (FileNotFoundError, OSError):
        raise NoSuchFileOrDirectoryException
    return [(await _serialize_row(row, csv_list_delimiter)) for row in data_from_csv]


async def _serialize_row(data: list, csv_list_delimiter: str):
    host = data[0]
    ports: list = list(map(int, filter(lambda x: x.isdigit(), data[1].split(csv_list_delimiter))))
    host_type = get_host_type(host)

    if not host_type: return NotValidRowCommand(domain=host, ports=ports)

    if host_type in ['domain', 'localhost']:
        domain = host
        ips = resolve_domain(host)
        if not ips: return NotValidRowCommand(domain=domain, ports=ports)
    else:
        domain = "???"
        ips = host.split(',')

    return FullRowCommand(domain=domain, ports=ports, ips=ips) if ports else PingCommand(domain=domain, ips=ips)


def read_csv_data(path: str, delimiter=CSV_DELIMITER) -> list:
    file_directory = FILES_DIRECTORY + validate_filename(path)
    with open(file_directory, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        return [row for row in reader][1:]

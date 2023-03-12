import os
from os import environ

from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILES_DIRECTORY = BASE_DIR + '/' + environ.get('FILES_DIRECTORY')
DURATION = environ.get('DURATION')
CSV_LIST_DELIMITER = environ.get('CSV_LIST_DELIMITER')
CSV_DELIMITER = environ.get('CSV_DELIMITER')
HOST_WAIT_TIMEOUT = int(environ.get('HOST_WAIT_TIMEOUT'))
CSV_SAVE_NEWLINE = environ.get('CSV_SAVE_NEWLINE')
RESULT_FILE_NAME = environ.get('RESULT_FILE_NAME')
PING_COUNT = int(environ.get('PING_COUNT'))
PORT_STATUS = {
    True: 'Opened',
    False: 'Unknown'
}

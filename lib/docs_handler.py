import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pathlib import Path


class DocHandler:
    def __init__(self, client_secret_path):
        '''
        Initialises the doc handler class
        :param client_secret_path: Path
        '''

        client_secret_path = client_secret_path  # type: Path

        if not client_secret_path.exists():
            raise FileNotFoundError

        self._scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        self._client_secret = client_secret_path

        self._credentials = ServiceAccountCredentials.from_json_keyfile_name(self._client_secret, self._scope)
        self._client = gspread.authorize(self._credentials)

    @property
    def client(self):
        '''
        Returns the client
        :return: gspread.client.Client
        '''
        return self._client

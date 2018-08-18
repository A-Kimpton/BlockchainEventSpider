from urllib.request import urlopen
from bs4 import BeautifulSoup

from lib.blockchain import BlockchainEvent


class WebScraper:
    def __init__(self, url):

        self._url = url
        self._soup = None
        self._blockchain_event_list = None  # type: list[BlockchainEvent]
        self._has_changed = False

    def run(self):
        '''
        This function would regenerate the blockchain_event_list if and only if the page has changed

        You generally don't want to override this method unless you plan on altering the circumstances of when a list
        should be updated.
        '''

        # Get and compare the web page soup
        old_soup = self._soup
        self._reload_page()
        self._has_changed = self._has_page_changed(old_soup)

        # If the page has changed then reset the event list
        if self._has_changed:
            self._blockchain_event_list = self._update_blockchain_event_list()

    def _update_blockchain_event_list(self):
        '''
        This hidden function should return a new list of blockchain events
        :return list[BlockchainEvent]:
        '''
        raise Exception("Override: def _update_blockchain_event_list(self)")

    def _has_page_changed(self, old_soup):
        '''
        This function is called to set the value of the _has_changed property
        :param old_soup:
        :return bool:
        '''
        raise Exception("Override: def _has_page_changed(self, old_soup)")

    def _reload_page(self):
        '''
        This is an internal function used to rerender the page
        :return:
        '''
        with urlopen(self._url) as web_page:
            self._soup = BeautifulSoup(web_page, 'html.parser')

    @property
    def has_content_changed(self):
        '''
        This function tests if between the last load of the page and current load of the page are the same
        :return bool:
        '''
        return self._has_changed

    @property
    def blockchain_event_list(self):
        '''
        Returns the lastest list of BlockchainEvents
        :return list[BlockchainEvent]:
        '''
        return self._blockchain_event_list

    @property
    def url(self):
        '''
        Returns the lastest list of BlockchainEvents
        :return:
        '''
        return self._url

    @property
    def soup(self):
        '''
        Returns the current page
        :return:
        '''
        return self._soup

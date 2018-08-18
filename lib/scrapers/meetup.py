from .web_scraper import WebScraper
from lib.blockchain import BlockchainEvent


class MeetupScraper(WebScraper):
    '''
    A web scraper for Meetup
    '''

    def __init__(self, url):
        '''
        Initialise my container for the soup and run the super init
        :param string url:
        '''

        self._page_items = None
        super().__init__(url)

    def _filter_soup(self, soup):
        '''
        A hidden function to filter the soup down to a dict
        :return:
        '''

        page_item_general = {
            'name': None,
            'page-url': None,
            'members': None,
            'location': None,
            'date': None
        }

        page_items = {}

        # Get a handle on the events
        html_all_events = soup.findAll('li', {'class': 'groupCard tileGrid-tile loading '})

        # extract all data I want
        for html_event in html_all_events:
            page_item = page_item_general

            page_unique_key = html_event['data-chapterid']

            page_item['name'] = html_event.div.a.text
            page_item['page-url'] = html_event.div.a['href']

            page_items[page_unique_key] = page_item

        return page_items

    def _has_page_changed(self, old_soup):
        '''
        Returns a bool value if the old soup is different to the new soup, and would be called after the page has been
        redownlaoded
        :param old_soup:
        :return bool:
        '''

        # In the event that old_soup is None, then the object must have changed
        if not old_soup:
            return True

        old_page_events = self._filter_soup(old_soup)
        new_page_events = self._filter_soup(self.soup)

        return old_page_events != new_page_events

    def _update_blockchain_event_list(self):
        '''
        This function should return a new list of blockchain events
        :return list[BlockchainEvent]:
        '''

        # Filter the soup for ease of making list
        self._page_items = self._filter_soup(self.soup)

        blockchain_list = list()

        for event_key in self._page_items:
            event = self._page_items[event_key]
            blockchain_list.append(
                BlockchainEvent(
                    eid=event_key,
                    data_dict=event
                )
            )

        return blockchain_list


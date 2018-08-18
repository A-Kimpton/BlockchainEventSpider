from lib.blockchain import BlockchainList
from lib.scrapers import WebScraper
from lib import DocHandler

from threading import Thread, Lock

import datetime


class ScraperHandler:
    def __init__(self, doc_handler, headings):
        '''

        :param DocHandler doc_handler:
        :param list headings:
        '''

        self._blockchain_events_lock = Lock()
        self._scrapers = list()  # type: list[WebScraper]

        with self._blockchain_events_lock:
            self._blockchain_events = BlockchainList(headings)

        self._doc_handler = doc_handler

        self._thread = Thread(target=self._run, name="web-spider")


    def start(self):
        '''
        This function will start the scraper
        :return:
        '''

        self._thread.start()


    def stop(self):
        '''
        This function will graciously stop the scraper
        :return:
        '''

        pass

    def add_scraper(self, scraper):
        '''

        :param WebScraper scraper:
        :return:
        '''

        if isinstance(scraper, WebScraper):
            self._scrapers.append(scraper)

    def _write_to_doc(self):
        print('[Info] Writing to doc...')

        data_sheet = self._doc_handler.client.open('Data').sheet1
        data_sheet.clear()

        data_sheet.append_row(['This data was collected by a spider', 'Last updated on: ' + str(datetime.date.today()), 'Created by A-Kimpton'])
        data_sheet.append_row([''])

        headings = self._blockchain_events.headings
        headings.append('Source')

        data_sheet.append_row(self._blockchain_events.headings)
        blockchain_items = self._blockchain_events.blockchain_items
        for source in blockchain_items:
            for blockchain_item in blockchain_items[source]:
                row = []

                for heading in self._blockchain_events.headings[:-1]:
                    heading = heading.lower()
                    blockchain_item.get_by_key(heading)
                    row.append(blockchain_item.get_by_key(key=heading))
                row.append(source)

                data_sheet.append_row(row)

        print('[Info] Writing complete!')

    def _run(self):

        # TODO: swap this loop out for multi threading! Currently only uses 1 (involves refactoring)
        print('[Info] Starting new web-thread')
        print('')

        with self._blockchain_events_lock:
            print('[Data]', self._blockchain_events)

        while True:
            for scraper in self._scrapers:
                scraper.run()
                if scraper.has_content_changed:
                    with self._blockchain_events_lock:
                        for blockchain_event in scraper.blockchain_event_list:
                            self._blockchain_events.append(blockchain_event, scraper.url)
                        print('[Info] New update has come in:', scraper.url)
                        print('[Data]', self._blockchain_events)
                        self._write_to_doc()

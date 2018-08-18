from lib.blockchain import BlockchainList
from lib.scrapers import WebScraper
from lib import DocHandler

from threading import Thread, Lock


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

    def _run(self, loop=0):
        # TODO: swap this loop out for multi threading! Currently only uses 1 (involves refactoring)
        print('[Info] Starting new web-thread')
        with self._blockchain_events_lock:
            print('[Data]', self._blockchain_events)
        while True:
            print('Loop: {}'.format(loop))
            loop += 1

            for scraper in self._scrapers:
                scraper.run()
                if scraper.has_content_changed:
                    with self._blockchain_events_lock:
                        for blockchain_event in scraper.blockchain_event_list:
                            self._blockchain_events.append(blockchain_event, scraper.url)
                        print('[Info] New update has come in:', scraper.url)
                        print('[Data]', self._blockchain_events)

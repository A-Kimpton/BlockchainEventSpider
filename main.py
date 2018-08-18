from lib import DocHandler, ScraperHandler, MeetupScraper
from pathlib import Path

import time

# DIR CONSTS
ROOT_DIR = Path(__file__).parent  # type: Path
DATA_DIR = ROOT_DIR / 'data'  # type: Path

# FILE CONSTS
CLIENT_SECRET = DATA_DIR / 'client_secret.json'  # type: Path


def main():
    '''
    This function is the main function in the program
    :return:
    '''
    doc_handler = get_doc_handler()

    scraper_handler = ScraperHandler(doc_handler, ['Name', 'URL'])
    for scraper in get_scrapers():
        scraper_handler.add_scraper(scraper)

    scraper_handler.start()


def get_scrapers():
    meetup_url = 'https://www.meetup.com/topics/blockchain/gb/17/london/?pageToken=default%7c100&country=gb&city=london&state=17&radius=25'

    scrapers = [
        MeetupScraper(meetup_url),
    ]

    return scrapers


def start_meetup(meetup_scraper, delay=1, updates=0):
    while meetup_scraper.has_page_not_changed():
        # Sleeps for delay seconds before pinging again
        print('[Info] Page not changed! - Page changed {} times'.format(updates))
        time.sleep(delay)

    # Page has changed!
    print('[Eureka] Page changed!')
    print(meetup_scraper.get_blockchain_list())

    # Start the tracker again
    start_meetup(meetup_scraper, delay, updates+1)

def get_doc_handler():
    '''
    Configures and returns a DocHandler obj
    :return: DocHandler
    '''

    doc_handler_obj = DocHandler(CLIENT_SECRET)

    return doc_handler_obj


if "__main__" == __name__:
    print('Program Started')
    main()

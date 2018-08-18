from . import BlockchainEvent


class BlockchainList:
    '''

    '''
    '''
    A class to hold records of blockchain events
    '''
    def __init__(self, headings):
        '''

        :param headings: list
        :param blockchain_items_iter: list[BlockchainItem]
        '''
        self._headings = headings
        self._blockchain_items = {

        }

    def append(self, blockchain_item, url):
        '''
        Adds a blockchain item to the list
        :param blockchain_item: BlockchainItem
        :return: bool
        '''
        if type(blockchain_item) is BlockchainEvent:
            if url in self._blockchain_items:
                self._blockchain_items[url].append(blockchain_item)
            else:
                self._blockchain_items[url] = [blockchain_item]
            return True
        return False

    def write_spreadsheet(self):
        pass

    @property
    def headings(self):
        return self._headings

    @property
    def blockchain_items(self):
        return self._blockchain_items

    def __repr__(self):
        return 'Data Lakes: {}, Headings: {}'.format(len(self.blockchain_items), self.headings)

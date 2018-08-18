class BlockchainEvent:
    '''
    A class to contain infomation about a particular event
    '''
    def __init__(self, eid, data_dict):
        '''

        :param object eid:
        :param dict data_dict:
        '''
        self._keys = data_dict.keys()
        self._data = data_dict
        self._id = eid

    @property
    def id(self):
        return self._id

    @property
    def headings(self):
        return self._keys

    @property
    def all_data(self):
        return self._data

    def get_by_key(self, key):
        if key in self._keys:
            return self._data[key]
        return None

    def __repr__(self):
        info = 'ID: {}'.format(self._id)
        for key in self._keys:
            info += ' - {}:{}'.format(key, self._data[key])
        return info

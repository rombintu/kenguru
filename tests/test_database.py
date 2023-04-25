import unittest
from store.store import Store

store = Store('sqlite:///:memory:')
uuids = [1234, 5678]

class TestStore(unittest.TestCase):
    def test_user_create(self):
        for uuid in uuids:
            print(store.user_create(uuid))

    def test_user_get_by_uuid(self):
        for uuid in uuids:
            print(store.user_get_by_uuid(uuid))

    def test_user_get_uuids(self):
        print(store.user_get_all_uuids())

    def test_user_get_all(self):
        print(store.user_get_all())

    def test_user_update(self):
        for uuid in uuids:
            store.user_update_activate(uuid, True) 

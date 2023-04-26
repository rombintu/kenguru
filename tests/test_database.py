import unittest
# from store.sqlite3 import Store
from store.mongodb import Store, User, Word

store = Store(mode="dev")
uuids = [1234, 5678]

class TestStore(unittest.TestCase):
    def test_user_create_one(self):
        for uuid in uuids:
            print(store.user_create_one(User(uuid)))

    def test_user_get_one(self):
        store.user_create_one(User(9999))
        for uuid in uuids:
            print(store.user_get_one(uuid))

    def test_user_get_all(self):
        store.user_create_one(User(9999))
        print(store.user_get_all())

    def test_user_update(self):
        for uuid in uuids:
            print(store.user_update_activate(uuid, True)) 
    
    def test_user_delete(self):
        for uuid in uuids:
            print(store.user_delete_one(uuid))

    def test_words_create_one(self):
        store.word_create_one(Word("sun", ["солнце"]))
        store.word_create_one(Word("moon", ["луна"], ["base", "test"]))
        print(store.word_get_many())
        print(store.word_get_many(tags=["test"]))


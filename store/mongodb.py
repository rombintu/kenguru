from pymongo import MongoClient
from pymongo_inmemory import MongoClient as MongoClientMem
from bson import ObjectId

MODE_DEV = "dev"
MODE_PROD = "prod"
DB_NAME = "kenguru"

class User:
    def __init__(self, uuid: int):
        # self._id = ObjectId()
        self.uuid = uuid
        self.activate = False

class Word:
    def __init__(self, en: str, ru: list[str], tags: list[str] = ["base"]):
        self.en = en
        self.ru = ru
        self.tags = tags

class Store:
    def __init__(self, connection=":memory:", mode="prod"):
        if mode != MODE_PROD:
            self.client = MongoClientMem()
        else: 
            self.client = MongoClient(connection)
        self.db = self.client[DB_NAME]

    # USER CRUD    
    def user_create_one(self, user: User):
        """Create user if uuid not exists and return login, else return login"""
        find_user = self.db.users.find_one({"uuid": user.uuid})
        if not find_user: 
            find_user = self.db.users.insert_one(user.__dict__)
        return find_user

    def user_update_activate(self, uuid: int, activate: bool):
        return self.db.users.update_one({"uuid": uuid}, {"$set": {"activate": activate}})

    def user_delete_one(self, uuid: int):
        return self.db.users.delete_one({"uuid": uuid})
            
    def user_get_all(self):
        return [user for user in self.db.users.find()]
            
    def user_get_one(self, uuid: int):
        return self.db.users.find_one({"uuid": uuid})
    
    # WORDS CRUD
    def word_get_one(self, _id: ObjectId):
        return self.db.words.find_one({"_id": _id})
            
    def word_get_many(self, tags=["all"]):
        if "all" in tags:
            return [word for word in self.db.words.find()]
        else:
            return [word for word in self.db.words.find({"tags": {"$all": tags}})]
            
    def word_create_one(self, word: Word):
        return self.db.words.insert_one(word.__dict__)
    
    def word_create_many(self, words: list[Word]):
        result = []
        for word in words:
            result.append(self.db.words.insert_many(word.__dict__))
        return result
    
    def word_delete_one(self, _id: ObjectId):
        return self.db.words.delete_one({"_id": _id})
    
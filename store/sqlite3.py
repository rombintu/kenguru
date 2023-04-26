# DEPRICATED

# external imports
from sqlalchemy import create_engine, Column, MetaData, Table
from sqlalchemy import insert, select, update, delete
from sqlalchemy import Integer, String, Boolean, ARRAY
from sqlalchemy.orm import declarative_base

Base = declarative_base()
Metadata = MetaData()

Users = Table(
    "users",
    Metadata,
    Column("_id", Integer, primary_key=True),
    Column("uuid", Integer, unique=True),
    Column("activate", Boolean),
)

Words = Table(
    "words",
    Metadata,
    Column("_id", Integer, primary_key=True),
    Column("en", String, unique=True),
    Column("ru", ARRAY(String)),
    Column("tag", ARRAY(String), default=["base"])
)

class User(Base):
    __table__ = Users

class Word(Base):
    __table__ = Words

class Store:
    def __init__(self, engine: str):
        self.engine = create_engine(engine)
        Metadata.create_all(self.engine)

    # USER CRUD    
    def user_create(self, uuid: int):
        """Create user if uuid not exists and return login, else return login"""
        with self.engine.connect() as c:
            with c.begin():
                select_user = select(User.uuid).where(User.uuid == uuid)
                login = c.execute(select_user).first()
                if not login:
                    create_user = (
                        insert(User).values(uuid=uuid, activate=False)
                    )
                    c.execute(create_user)
                    c.commit()
                    login = c.execute(select_user).first()
                return login

    def user_update_activate(self, uuid: int, activate: bool):
        with self.engine.connect() as c:
            with c.begin():
                activate = update(User).where(User.uuid == uuid).values(activate=activate)
                c.execute(activate)
                c.commit()

    def user_delete(self, uuid: int):
        with self.engine.connect() as c:
            with c.begin():
                delete_user_exec = delete(User).where(User.uuid == uuid)
                try:
                    c.execute(delete_user_exec)
                    c.commit()
                except Exception as err:
                    return err
                return None
            
    def user_get_all(self):
        with self.engine.connect() as c:
            with c.begin():
                users_exec = select(User)
                return c.execute(users_exec).all()
            
    def user_get_all_uuids(self):
        with self.engine.connect() as c:
            with c.begin():
                users_exec = select(User.uuid)
                return c.execute(users_exec).all()
            
    def user_get_by_uuid(self, uuid: int):
        with self.engine.connect() as c:
            with c.begin():
                user_exec = select(User).where(User.uuid == uuid)
                return c.execute(user_exec).one()
    
    # WORDS CRUD
    def word_get_one(self, _id: int):
        with self.engine.connect() as c:
            with c.begin():
                word_exec = select(Word).where(Word._id == _id)
                return c.execute(word_exec).one()
            
    def word_get_many(self, tags=["all"]):
        with self.engine.connect() as c:
            with c.begin():
                word_exec = select(Word).where(Word.tags == tags)
                if "all" in tags:
                    word_exec = select(Word)
                return c.execute(word_exec).all()
            
    def word_create_one(self, word: dict):
        with self.engine.connect() as c:
            with c.begin():
                word_exec = insert(Word).values(word)
                c.execute(word_exec)
                c.commit()
    
    def word_create_many(self, words: list[dict]):
        with self.engine.connect() as c:
            with c.begin():
                word_exec = insert(Word).values(words)
                c.execute(word_exec)
                c.commit()
                
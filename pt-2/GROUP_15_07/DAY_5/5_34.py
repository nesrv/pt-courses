from sqlalchemy import *
from sqlalchemy.orm import *

sqlite_database = "sqlite:///product.db"
engine = create_engine(sqlite_database, echo=False)

class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return self.name

    def as_dict(self):
        return {obj.name: getattr(self, obj.name) for obj in self.__table__.columns}

    def dump_to_fixture(self):
        ...
        #запись в json -файл

class Company(Base):




def get_user_by_id(id=2):
    with Session(autoflush=False, bind=engine) as db:
        user = db.get(Person, id)
        user_dict = user.as_dict()
        print(user_dict)

get_user_by_id(id=2)

# Base.metadata.create_all(bind=engine)

# плюс в чат , если бд появилась

# CRUD

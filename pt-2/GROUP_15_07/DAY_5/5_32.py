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


# Base.metadata.create_all(bind=engine)

# плюс в чат , если бд появилась

# CRUD
def create_users():
    with Session(autoflush=False, bind=engine) as db:
        user1 = Person(name="Сергей", age=21)
        user2 = Person(name="Татьяна", age=18)
        db.add_all((user1, user2))
        db.commit()


def read_users():
    with Session(autoflush=False, bind=engine) as db:
        users = db.query(Person).all()
        # for user in users:
        #     print(user.name, user.age)
        print(users)


def get_user_by_id(id=1):
    with Session(autoflush=False, bind=engine) as db:
        user = db.get(Person, id)
        print(user)


def get_filtered_user(age):
    with Session(autoflush=False, bind=engine) as db:
        users = db.query(Person).filter(Person.age > age)
        print(*users)


def get_user_by_filter(id):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Person).filter(Person.id == id).first()
        print(user)


def update_user(id=1):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Person).filter(Person.id == id).first()
        user.name = "Наталья"
        user.age = 19
        db.commit()

def update_all_users():
    with Session(autoflush=False, bind=engine) as db:
        users = db.query(Person).all()
        for user in users:
            user.age += 10
        db.commit()

def del_user_by_id(id):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Person).filter(Person.id == id).first()
        db.delete(user)
        db.commit()

# del_user_by_id(1)
# update_all_users()
# update_user(id=2)
# read_users()
# get_user_by_id(2)
# get_filtered_user(20)
# get_user_by_filter(3)

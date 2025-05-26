from sqlalchemy import *
from sqlalchemy.orm import *

sqlite_database = "sqlite:///product1.db"
engine = create_engine(sqlite_database, echo=False)

class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    company_id = Column(Integer, ForeignKey("companies.id"))  # one-to-many
    company = relationship("Company", back_populates="users")  # one-to-many

    def __repr__(self):
        return self.name

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship("Person", back_populates="company")

    def __repr__(self):
        return f"Company(id={self.id}, name={self.name})"


def add_test_date_db():
    with Session(autoflush=False, bind=engine) as db:
        microsoft = Company(name="Microsoft")
        google = Company(name="Google")
        db.add_all([microsoft, google])

        db.commit()

        # google = db.query(Company).filter(Company.name == "Google").first()

        user1 = Person(name="Сергей", age=28)
        user2 = Person(name="Владимир", age=32)

        user1.company = microsoft
        user2.company = google

        db.add_all([user1, user2])
        db.commit()

def get_users_from_companies():
    with Session(autoflush=False, bind=engine) as db:
        companies = db.query(Company).all()
        for comp in companies:
            print(comp.name, end=" : ")
            for user in comp.users:
                print(user)


get_users_from_companies()
# add_test_date_db()



# Base.metadata.create_all(bind=engine)


# Base.metadata.create_all(bind=engine)

# плюс в чат , если бд появилась

# CRUD

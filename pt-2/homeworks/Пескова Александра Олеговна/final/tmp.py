from sqlalchemy import *
from sqlalchemy.orm import *


engine = create_engine('sqlite:///tmp.db', echo=True)

class Base(DeclarativeBase):
    ...

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    paysys_id = Column(Integer, ForeignKey('PaymentSystems.id'))
    number = relationship("PaymentSystems", back_populates="card")
    owner = Column(String)


class PaymentSystems(Base):
    __tablename__ = 'paysystems'

    id = Column(Integer, primary_key=True, index=True)
    paysys = Column(String)
    works = Column(String)
    card = relationship("Card", back_populates="number", cascade='all, delete-orphan')


    def __str__(self):
        return f'{self.paysys}, {self.works} тут'



Base.metadata.create_all(engine)


def add_paysys():
    with Session(autoflush=False, bind=engine) as db:
        mir = PaymentSystems(paysys='Мир', works='Работает')
        dc = PaymentSystems(paysys='DinersClub', works='Работает')
        visa = PaymentSystems(paysys='VISA', works='Работает')
        mc = PaymentSystems(paysys='MasterCard', works='Работает')
        cup = PaymentSystems(paysys='China UnionPay', works='Работает')
        uek = PaymentSystems(paysys='УЭК', works='Работает')
        jcb = PaymentSystems(paysys='JCB Interntional', works='Не работает')
        amex = PaymentSystems(paysys='American Express', works='Не работает')
        maestro = PaymentSystems(paysys='Maestro', works='Не работает')
        discover = PaymentSystems(paysys='Discover', works='Не работает')
        db.add_all([mir, dc, visa, mc, cup, uek, jcb, amex, maestro, discover])
        db.commit()

# add_paysys()

def remove_extra(status):
    with Session(autoflush=False, bind=engine) as db:
        paysys = db.query(PaymentSystems).filter(PaymentSystems.works == status).first()
        db.delete(paysys)
        db.commit()

# remove_extra('Работает')

def add_cards():
    with Session(autoflush=False, bind=engine) as db:
        visa = Card(number='4274991000171851', owner='Иван Иванов')
        maestro = Card(number='5019555544445555', owner='Joe Biden')
        db.add_all([visa, maestro])
        db.commit()



add_cards()
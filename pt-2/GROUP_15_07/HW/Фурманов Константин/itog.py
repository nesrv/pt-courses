def luhn_check(card_number: str) -> bool:
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0
from enum import Enum

class PaySystem(Enum):
    MIR = "Мир"
    AMERICAN_EXPRESS = "American Express"
    JCB = "JCB International"
    DINERS_CLUB = "Diners Club"
    VISA = "VISA"
    MASTERCARD = "MasterCard"
    MAESTRO = "Maestro"
    CHINA_UNIONPAY = "China UnionPay"
    DISCOVER = "Discover"
    UEC = "УЭК"

    @staticmethod
    def get_pay_system(card_number: str):
        if card_number.startswith("2"):
            return PaySystem.MIR
        if card_number.startswith("3"):
            if card_number.startswith(("34", "37")):
                return PaySystem.AMERICAN_EXPRESS
            if card_number.startswith(("31", "35")):
                return PaySystem.JCB
            if card_number.startswith(("30", "36", "38")):
                return PaySystem.DINERS_CLUB
        if card_number.startswith("4"):
            return PaySystem.VISA
        if card_number.startswith("5"):
            if card_number.startswith(("51", "52", "53", "54", "55")):
                return PaySystem.MASTERCARD
            if card_number.startswith(("50", "56", "57", "58")):
                return PaySystem.MAESTRO
        if card_number.startswith("6"):
            if card_number.startswith("60"):
                return PaySystem.DISCOVER
            if card_number.startswith("62"):
                return PaySystem.CHINA_UNIONPAY
            if card_number.startswith(("63", "67")):
                return PaySystem.MAESTRO
        if card_number.startswith("7"):
            return PaySystem.UEC
        return None

class Card:
    def __init__(self, card_number: str, cardholder_name: str):
        self.card_number = card_number.replace(" ", "")
        self.cardholder_name = cardholder_name
        self.pay_system = PaySystem.get_pay_system(self.card_number)

    def is_valid(self):
        return luhn_check(self.card_number)

    def __repr__(self):
        return f"{self.cardholder_name}: {self.card_number} ({self.pay_system.name if self.pay_system else 'Unknown'})"

class CardBank:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        if card.is_valid():
            self.cards.append(card)

    def __str__(self):
        return "\n".join(str(card) for card in self.cards)

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.future import select

Base = declarative_base()
engine = create_engine("sqlite:///cardbank.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

class CardDB(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String, unique=True, index=True)
    cardholder_name = Column(String)
    pay_system = Column(String)
    is_valid = Column(String)

Base.metadata.create_all(bind=engine)

class CardBankDatabase:
    def __init__(self):
        self.db = SessionLocal()

    def create_card(self, card: Card):
        db_card = CardDB(card_number=card.card_number,
                         cardholder_name=card.cardholder_name,
                         pay_system=card.pay_system.name if card.pay_system else 'Unknown',
                         is_valid=str(card.is_valid()))
        self.db.add(db_card)
        self.db.commit()
        self.db.refresh(db_card)
        return db_card

    def read_cards(self):
        return self.db.execute(select(CardDB)).scalars().all()

    def update_card(self, card_id: int, name: str, card_number: str):
        db_card = self.db.query(CardDB).filter(CardDB.id == card_id).first()
        if db_card:
            db_card.cardholder_name = name
            db_card.card_number = card_number
            self.db.commit()
            self.db.refresh(db_card)
        return db_card

    def delete_card(self, card_id: int):
        db_card = self.db.query(CardDB).filter(CardDB.id == card_id).first()
        if db_card:
            self.db.delete(db_card)
            self.db.commit()

db = CardBankDatabase()
import asyncio
from databases import Database

DATABASE_URL = "sqlite:///cardbank.db"
database = Database(DATABASE_URL)


class AsyncCardBankDatabase:
    async def create_card(self, card: Card):
        query = """
        INSERT INTO cards (card_number, cardholder_name, pay_system, is_valid)
        VALUES (:card_number, :cardholder_name, :pay_system, :is_valid)
        """
        values = {
            "card_number": card.card_number,
            "cardholder_name": card.cardholder_name,
            "pay_system": card.pay_system.name if card.pay_system else 'Unknown',
            "is_valid": str(card.is_valid())
        }
        await database.execute(query=query, values=values)

    async def read_cards(self):
        query = "SELECT * FROM cards"
        return await database.fetch_all(query=query)

    async def update_card(self, card_id: int, name: str, card_number: str):
        query = """
        UPDATE cards
        SET cardholder_name = :name, card_number = :card_number
        WHERE id = :card_id
        """
        values = {
            "card_id": card_id,
            "name": name,
            "card_number": card_number
        }
        await database.execute(query=query, values=values)

    async def delete_card(self, card_id: int):
        query = "DELETE FROM cards WHERE id = :card_id"
        values = {"card_id": card_id}
        await database.execute(query=query, values=values)


async def main():
    await database.connect()
    async_db = AsyncCardBankDatabase()

    # Пример создания карты
    card = Card("4274991000171851", "Иван Иванов")
    await async_db.create_card(card)

    # Пример чтения карт
    cards = await async_db.read_cards()
    print(cards)

    await database.disconnect()


asyncio.run(main())

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NULLTYPE
from sqlalchemy.testing.util import function_named


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "student"

    student_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    phone_number: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"User(id={self.id}, first name={self.first_name}, last name = {self.last_name})"

from sqlalchemy import create_engine
engine = create_engine("sqlite:///mydb.db", echo=True)

Base.metadata.create_all(engine)

from sqlalchemy.orm import Session

def add_base_users():
    global Session
    with Session(engine) as Session:
        Leo = User(
            student_id = 3,
            first_name = "Leo",
            last_name = "Tieu",
        )
        Milo = User(
            student_id = 4,
            first_name = "Milo",
            last_name = "Like",
            phone_number = "12345678"
        )
        Session.add_all([Leo, Milo])
        Session.commit()


if __name__ == '__main__':
    add_base_users()

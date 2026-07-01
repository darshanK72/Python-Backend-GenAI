# 02 — SQLAlchemy test session with in-memory SQLite
# Run: pytest 02_sqlalchemy_test_session.py -v

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    pass


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)


def make_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()


def test_orm_crud():
    session = make_session()
    session.add(Note(title="ORM note"))
    session.commit()
    rows = session.query(Note).all()
    session.close()
    assert len(rows) == 1
    assert rows[0].title == "ORM note"

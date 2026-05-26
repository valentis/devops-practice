from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

_write_engine = create_engine("postgresql://user:pass@primary/db", pool_size=10)
_read_engine  = create_engine("postgresql://user:pass@replica/db", pool_size=20)

WriteSession = sessionmaker(bind=_write_engine)
ReadSession  = sessionmaker(bind=_read_engine)

@contextmanager
def get_db_write():
    """INSERT / UPDATE / DELETE 전용 세션"""
    db = WriteSession()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

@contextmanager
def get_db_read():
    """SELECT 전용 세션 (레플리카)"""
    db = ReadSession()
    try:
        yield db
    finally:
        db.close()

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_DATABASE")
charset_type = "utf8mb4"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset={charset_type}"
)

SessionClass = sessionmaker(
    bind=engine,
    autocommit=False,
    expire_on_commit=False
)  # セッションを作るクラスを作成


class Session:
    def __init__(self, session: SessionClass = SessionClass()):
        self.session = session

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()

from .database import Base, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event

from .crud import user_repo
from .responses import response
from contextlib import contextmanager


def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')

@contextmanager
def get_db():

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    event.listen(engine, 'connect', _fk_pragma_on_connect)

    # Base = declarative_base()
    Base.metadata.create_all(engine)

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(request):
    with get_db() as session:
        user = user_repo.create_user(session, request)
        if user:
            return response.UserResponse(status=1, msg="success", data=[user])
        else:
            return response.UserResponse(status=-1, msg="internal database error", data=[])

def get_user_by_user_name(request):
    with get_db() as session:
        user = user_repo.get_user_by_user_name(session, request.user_name)
        if user:
            return response.UserResponse(status=1, msg="success", data=[user])
        else:
            return response.UserResponse(status=-1, msg="internal database error", data=[])


def get_all_users():
    with get_db() as session:
        users = user_repo.get_all_users(session)
        if len(users):
            return response.UserResponse(status=1, msg="success", data=users)
        else:
            return response.UserResponse(status=-1, msg="no existing users", data=[])

def recover_users(users):
    with get_db() as session:
        res = user_repo.recover_users(session, users)
        if res is not None:
            return 0

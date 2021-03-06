from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from ..models.user import User

from ..schemas.user import UserRegister


def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user
    return None


def get_user_by_user_name(db: Session, user_name: str):
    res = db.query(User).filter(User.user_name == user_name)
    # print(res)
    # print(user_name)
    # print(res.first())
    user = res.first()
    if user:
        return user
    else:
        return None


def get_all_users(db: Session):
    # users = db.query(User).limit(limit).all()
    users = db.query(User).all()
    return users


def create_user(db: Session, user: UserRegister):
    db_user = User(id=user.id,
                   user_name=user.user_name,
                   password=user.password,)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except SQLAlchemyError as e:
        db.rollback()
        return None

    return db_user

def recover_users(db: Session, users):
    users_to_add = []
    for user in users:
        cur_user = User(id=user.id, user_name=user.user_name, password=user.password)
        users_to_add.append(cur_user)
    try:
        db.add_all(users_to_add)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        return None

    return "success"

def get_name_by_id_list(db: Session, id_list):
    name_list = []
    res = db.query(User).filter(User.id.in_(id_list)).all()
    for i in res:
        name_list.append(i.user_name)
    return name_list

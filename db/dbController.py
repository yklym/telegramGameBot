from db.loader import session
from db.models.user import User


class DbController:

    def __init__(self, session):
        self._session = session

    def get_user(self, user):
        qr_res = self._session.query(User).filter(User.id == user.id).first()
        return qr_res

    def add_user(self, user):
        new_user = User(id=user.id, name=user.first_name,
                        fullname=user.first_name + user.last_name if user.last_name else "",
                        nickname=user.username)
        session.add(new_user)
        session.commit()


dbController = DbController(session)

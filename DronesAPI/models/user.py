from DronesAPI.database.db import db


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String())
    team = db.Column(db.String())

    def __init__(self, username, password, team):
        self.username = username
        self.password = password
        self.team = team

    def json(self):
        """
        This method returns a dict containing the object data, to be returned easily
        """
        return {
            "id": self.id,
            "username": self.username,
            "team": self.team
        }

    def save_to_db(self):
        """
        Method to save user to DB
        """
        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        """
        Method to remove user from DB
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_user_by_username(cls, username):
        """
         Class method which finds user from DB by username
        :param username: the user name
        :return: single db entry
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_user_by_id(cls, _id):
        """
        Class method which finds user from DB by id
        :param _id: the user id
        :return: single db entry
        """
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all_users(cls, ):
        """
        Class method which lists all users from DB
        :return: list of db entries
        """
        return cls.query.all()

    # Class method which lists all users from DB sorted by name
    @classmethod
    def find_users_by_name(cls):
        """
        Class method which lists all users from DB sorted by name
        :return: list of db entries
        """
        return cls.query.order_by('username').all()

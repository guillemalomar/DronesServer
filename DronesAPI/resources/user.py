import logging
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token,\
                               create_refresh_token,\
                               jwt_refresh_token_required,\
                               get_jwt_identity,\
                               fresh_jwt_required,\
                               get_current_user

from DronesAPI.models.user import UserModel
from DronesAPI.creds import ADMIN_SECRET_KEY

import hashlib

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username",
    type=str,
    required=True,
    help="This field cannot be blank"
)
_user_parser.add_argument(
    "password",
    type=str,
    required=True,
    help="This field cannot be blank"
)
_user_parser.add_argument(
    "team",
    type=str,
    required=False,
    help="This field can be blank"
)
_user_parser.add_argument(
    "secret_key",
    type=str,
    required=False,
    help="This field can be blank"
)


class User(Resource):
    @staticmethod
    def get(user_id):
        """
        Static method that fetches and returns the user entry with a specific id
        :param user_id: user id
        :return: a dict with the camera data / an error message
        """
        user = UserModel.find_user_by_id(user_id)
        if user:
            logging.info(user.json())
            return user.json()

        logging.info("User not found")
        return {
                   "message": "User not found"
               }, 404

    @fresh_jwt_required
    def delete(self, user_id):
        """
        Static method that fetches and deletes the user entry with a specific id.
        Can only be done if the user logged in is a support team user.
        :param user_id: user id
        :return: a success message / an error message
        """
        user_team = UserModel.find_user_by_id(get_current_user()).team
        if user_team == 'Support':
            user = UserModel.find_user_by_id(user_id)
            if user:
                user.remove_from_db()
                logging.info("User deleted")
                return {
                           "message": "User deleted"
                       }

            logging.info("User not found")
            return {
                       "message": "User not found"
                   }, 404
        else:
            logging.error("Unauthorized user")
            return {
                       "message": "Non authorized user"
                   }, 400


class Users(Resource):
    @staticmethod
    def get():
        """
        Static method that fetches and returns all users
        :return: a list of dicts with the users data / an error message
        """
        users = UserModel.find_all_users()
        if users:
            output = {}
            for ind, user in enumerate(users):
                output[str(ind)] = user.json()
            logging.info(output)
            return output

        logging.error("Users not found")
        return {
                   "message": "Users not found"
               }, 404


class UsersByName(Resource):
    @staticmethod
    def get():
        """
        Static method that fetches and returns all users, sorted by name
        :return: a list of dicts with the users data / an error message
        """
        users = UserModel.find_users_by_name()
        if users:
            output = {}
            for ind, user in enumerate(users):
                output[str(ind)] = user.json()
            logging.info(output)
            return output
        logging.info("Users not found")
        return {
                   "message": "Users not found"
               }, 404


class UserAdminRegister(Resource):
    @staticmethod
    def post():
        """
        Method saves a new admin user.
        :return: a success message / error message
        """
        data = _user_parser.parse_args()
        if data['secret_key'] == ADMIN_SECRET_KEY:
            if UserModel.find_user_by_username(data["username"]):
                logging.info("User already exists")
                return {
                           "message": "User already exists"
                       }, 400

            user = UserModel(data["username"],
                             hashlib.sha256(data["password"].encode("utf-8")).hexdigest(),
                             data['team'])
            user.save_to_db()
            logging.info("User {} created".format(data["username"]))
            return {
                "message": "User {} created".format(data["username"])
            }
        else:
            logging.info("Unloged users cannot created users without a correct secret_key")
            return {
                       "message": "Unloged users cannot created users without a correct secret_key"
                   }, 400


class UserRegister(Resource):
    @staticmethod
    @fresh_jwt_required
    def post():
        """
        Method saves a new user.
        Can only be done if the user logged in is a support team user.
        :return: a success message / error message
        """
        data = _user_parser.parse_args()
        user = get_current_user()
        if user:
            user_team = UserModel.find_user_by_id(user).team
            if user_team == 'Support':
                if UserModel.find_user_by_username(data["username"]):
                    logging.info("User already exists")
                    return {
                               "message": "User already exists"
                           }, 400

                user = UserModel(data["username"],
                                 hashlib.sha256(data["password"].encode("utf-8")).hexdigest(),
                                 data['team'])
                user.save_to_db()
                logging.info("User {} created".format(data["username"]))
                return {
                    "message": "User {} created".format(data["username"])
                }
            else:
                logging.info("Non authorized user")
                return {
                           "message": "Non authorized user"
                       }, 400
        else:
            logging.info("Unlogged users cannot create other users")
            return {
                       "message": "Unlogged users cannot create other users"
                   }, 400


class UserLogin(Resource):
    @staticmethod
    def post():
        """
        This method checks if the user that is trying to login is a registered user, and returns authentication data
        :return: a dict with authentication tokens / an error message
        """
        data = _user_parser.parse_args()

        user = UserModel.find_user_by_username(data["username"])

        if user and user.password == hashlib.sha256(data["password"].encode("utf-8")).hexdigest():
            access_token = create_access_token(identity=user.id, fresh=True)  # Puts User ID as Identity in JWT
            refresh_token = create_refresh_token(identity=user.id)  # Puts User ID as Identity in JWT
            logging.info("Login credentials obtained")
            return {
                       "access_token": access_token,
                       "refresh_token": refresh_token
                   }
        logging.info("Invalid credentials")
        return {
                   "message": "Invalid credentials"
               }, 401


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user_id = get_jwt_identity()  # Gets Identity from JWT
        new_token = create_access_token(identity=current_user_id, fresh=False)
        return {
                   "access_token": new_token
               }

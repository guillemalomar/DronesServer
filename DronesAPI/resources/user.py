from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token,\
                               create_refresh_token,\
                               jwt_refresh_token_required,\
                               get_jwt_identity,\
                               fresh_jwt_required,\
                               get_current_user

from DronesAPI.models.user import UserModel
from DronesAPI.creds import admin_secret_key

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
        user = UserModel.find_user_by_id(user_id)
        if user:
            return user.json()

        return {
                   "message": "User not found!"
               }, 404

    @fresh_jwt_required
    def delete(self, user_id):
        user = UserModel.find_user_by_id(user_id)
        if user:
            user.remove_from_db()
            return {
                       "message": "User deleted!"
                   }

        return {
                   "message": "User not found!"
               }, 404


class Users(Resource):
    @staticmethod
    def get():
        users = UserModel.find_all_users()
        if users:
            output = {}
            for ind, user in enumerate(users):
                output[str(ind)] = user.json()
            return output

        return {
                   "message": "Users not found!"
               }, 404


class UsersByName(Resource):
    @staticmethod
    def get():
        users = UserModel.find_users_by_name()
        if users:
            output = {}
            for ind, user in enumerate(users):
                output[str(ind)] = user.json()
            return output

        return {
                   "message": "Users not found!"
               }, 404


class UserAdminRegister(Resource):
    @staticmethod
    def post():
        data = _user_parser.parse_args()
        if data['secret_key'] == admin_secret_key:
            if UserModel.find_user_by_username(data["username"]):
                return {
                           "message": "User exists!"
                       }, 400

            user = UserModel(data["username"],
                             hashlib.sha256(data["password"].encode("utf-8")).hexdigest(),
                             data['team'])
            user.save_to_db()
            return {
                "message": "User {} created!".format(data["username"])
            }
        else:
            return {
                       "message": "Unloged users cannot created users without a correct secret_key!"
                   }, 400


class UserRegister(Resource):
    @staticmethod
    @fresh_jwt_required
    def post():
        data = _user_parser.parse_args()
        user = get_current_user()
        if user:
            user_team = UserModel.find_user_by_id(user).team
            if user_team == 'Support':
                if UserModel.find_user_by_username(data["username"]):
                    return {
                               "message": "User exists!"
                           }, 400

                user = UserModel(data["username"],
                                 hashlib.sha256(data["password"].encode("utf-8")).hexdigest(),
                                 data['team'])
                user.save_to_db()
                return {
                    "message": "User {} created!".format(data["username"])
                }
            else:
                return {
                           "message": "Non authorized user!"
                       }, 400
        else:
            return {
                       "message": "Unlogged users cannot create other users!"
                   }, 400


class UserLogin(Resource):
    @staticmethod
    def post():
        data = _user_parser.parse_args()

        user = UserModel.find_user_by_username(data["username"])

        if user and user.password == hashlib.sha256(data["password"].encode("utf-8")).hexdigest():
            access_token = create_access_token(identity=user.id, fresh=True)  # Puts User ID as Identity in JWT
            refresh_token = create_refresh_token(identity=user.id)  # Puts User ID as Identity in JWT

            return {
                       "access_token": access_token,
                       "refresh_token": refresh_token
                   }

        return {
                   "message": "Invalid credentials!"
               }, 401


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user_id = get_jwt_identity()  # Gets Identity from JWT
        new_token = create_access_token(identity=current_user_id, fresh=False)
        return {
                   "access_token": new_token
               }

from flask_restful import Resource, reqparse
from flask_jwt_extended import fresh_jwt_required, get_current_user

from DronesAPI.models.camera import CameraModel
from DronesAPI.models.user import UserModel

_drone_parser = reqparse.RequestParser()
_drone_parser.add_argument(
    "model",
    type=str,
    required=False,
    help="This field can be blank"
)
_drone_parser.add_argument(
    "megapixels",
    type=float,
    required=False,
    help="This field can be blank"
)
_drone_parser.add_argument(
    "brand",
    type=str,
    required=False,
    help="This field can be blank"
)


class Camera(Resource):
    @staticmethod
    def get(model):
        camera = CameraModel.find_camera_by_model(model)
        if camera:
            return camera.json()
        return {
                   "message": "Camera not found!"
               }, 404

    @staticmethod
    @fresh_jwt_required
    def delete(model):
        user_team = UserModel.find_user_by_id(get_current_user()).team
        if user_team == 'Support':
            camera = CameraModel.find_camera_by_model(model)
            if camera:
                camera.remove_from_db()
                return {
                           "message": "Camera deleted!"
                       }

            return {
                       "message": "Camera not found!"
                   }, 404
        else:
            return {
                       "message": "Non authorized user!"
                   }, 400


class Cameras(Resource):
    @staticmethod
    def get():
        cameras = CameraModel.find_all_cameras()
        if cameras:
            output = []
            for camera in cameras:
                output.append(camera.json())
            return output

        return {
                   "message": "No cameras found!"
               }, 404


class CamerasByModel(Resource):
    @staticmethod
    def get():
        cameras = CameraModel.sort_cameras_by_model()
        if cameras:
            output = []
            for camera in cameras:
                output.append(camera.json())
            return output

        return {
                   "message": "No cameras found!"
               }, 404


class CameraRegister(Resource):

    @fresh_jwt_required
    def post(self):
        user_team = UserModel.find_user_by_id(get_current_user()).team
        if user_team == 'Support':
            data = _drone_parser.parse_args()

            if CameraModel.find_camera_by_model(data["model"]):
                return {
                           "message": "Camera exists!"
                       }, 400

            drone = CameraModel(data["model"], data["megapixels"], data["brand"])
            drone.save_to_db()
            return {
                "message": "Camera {} created!".format(data["model"])
            }
        else:
            return {
                       "message": "Non authorized user!"
                   }, 400

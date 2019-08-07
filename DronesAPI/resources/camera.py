import logging
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
        """
        Static method that fetches and returns the camera entry with a specific model
        :param model: camera model
        :return: a dict with the camera data / an error message
        """
        camera = CameraModel.find_camera_by_model(model)
        if camera:
            logging.info(camera.json())
            return camera.json()
        logging.info("Camera not found!")
        return {
                   "message": "Camera not found!"
               }, 404

    @staticmethod
    @fresh_jwt_required
    def delete(model):
        """
        Static method that fetches and deletes the camera entry with a specific model.
        Can only be done if the user logged in is a support team user.
        :param model: camera model
        :return: a success message / an error message
        """
        user_team = UserModel.find_user_by_id(get_current_user()).team
        if user_team == 'Support':
            camera = CameraModel.find_camera_by_model(model)
            if camera:
                camera.remove_from_db()
                logging.info("Camera deleted!")
                return {
                           "message": "Camera deleted!"
                       }
            logging.info("Camera not found!")
            return {
                       "message": "Camera not found!"
                   }, 404
        else:
            logging.info("Non authorized user!")
            return {
                       "message": "Non authorized user!"
                   }, 400


class Cameras(Resource):
    @staticmethod
    def get():
        """
        Static method that fetches and returns all cameras
        :return: a list of dicts with the cameras data / an error message
        """
        cameras = CameraModel.find_all_cameras()
        if cameras:
            output = []
            for camera in cameras:
                output.append(camera.json())
            logging.info(output)
            return output

        logging.info("No cameras found!")
        return {
                   "message": "No cameras found!"
               }, 404


class CamerasByModel(Resource):
    @staticmethod
    def get():
        """
        Static method that fetches and returns all cameras, sorted by model
        :return: a list of dicts with the cameras data / an error message
        """
        cameras = CameraModel.sort_cameras_by_model()
        if cameras:
            output = []
            for camera in cameras:
                output.append(camera.json())
            logging.info(output)
            return output

        logging.info("No cameras found!")
        return {
                   "message": "No cameras found!"
               }, 404


class CameraRegister(Resource):

    @fresh_jwt_required
    def post(self):
        """
        Method saves a new camera.
        Can only be done if the user logged in is a support team user.
        :return: a success message / error message
        """
        user_team = UserModel.find_user_by_id(get_current_user()).team
        if user_team == 'Support':
            data = _drone_parser.parse_args()

            if CameraModel.find_camera_by_model(data["model"]):
                logging.info("The camera already exists")
                return {
                           "message": "The camera already exists!"
                       }, 400

            drone = CameraModel(data["model"], data["megapixels"], data["brand"])
            drone.save_to_db()
            logging.info("Camera {} created!".format(data["model"]))
            return {
                "message": "Camera {} created!".format(data["model"])
            }
        else:
            logging.info("Non authorized user!")
            return {
                       "message": "Non authorized user!"
                   }, 400

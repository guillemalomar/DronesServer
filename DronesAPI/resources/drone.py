import logging
from flask_restful import Resource, reqparse
from flask_jwt_extended import fresh_jwt_required, get_current_user

from DronesAPI.models.drone import DroneModel
from DronesAPI.models.camera import CameraModel
from DronesAPI.models.user import UserModel

_drone_parser = reqparse.RequestParser()
_drone_parser.add_argument(
    "serial_number",
    type=str,
    required=False,
    help="This field can be blank"
)
_drone_parser.add_argument(
    "name",
    type=str,
    required=False,
    help="This field can be blank"
)
_drone_parser.add_argument(
    "brand",
    type=str,
    required=False,
    help="This field can be blank"
)
_drone_parser.add_argument(
    "cameras",
    type=str,
    required=False,
    help="This field can be blank"
)


class DroneBySerial(Resource):
    @staticmethod
    @fresh_jwt_required
    def get(serial_number):
        """
        Static method that fetches and returns the drone entry with a specific serial number
        :param serial_number: camera model
        :return: a dict with the drone data / an error message
        """
        drone = DroneModel.find_drone_by_serial(serial_number)
        if drone:
            logging.info(process_cameras(drone))
            return process_cameras(drone)
        logging.info("No drone found")
        return {
                   "message": "Drone not found"
               }, 404

    @staticmethod
    @fresh_jwt_required
    def delete(serial_number):
        """
        Static method that fetches and deletes the drone entry with a specific serial number.
        Can only be done if the user logged in is a support team user.
        :param serial_number: drone serial number
        :return: a success message / an error message
        """
        user_team = UserModel.find_user_by_id(get_current_user()).team
        if user_team == 'Support':
            drone = DroneModel.find_drone_by_serial(serial_number)
            if drone:
                drone.remove_from_db()
                logging.info("Drone deleted")
                return {
                           "message": "Drone deleted"
                       }
            logging.info("No drone found")
            return {
                       "message": "Drone not found"
                   }, 404
        else:
            logging.info("Non authorized user")
            return {
                       "message": "Non authorized user"
                   }, 400


class DroneByName(Resource):
    @staticmethod
    @fresh_jwt_required
    def get(name):
        """
        Static method that fetches and returns the drone entries with a specific name
        :param name: camera model
        :return: a list of dicts with the drones data / an error message
        """
        drones = DroneModel.find_drones_by_name(name)
        if drones:
            output = []
            for drone in drones:
                output.append(process_cameras(drone))
            logging.info(output)
            return output
        logging.info("No drones found")
        return {
                   "message": "Drone not found"
               }, 404


class Drones(Resource):
    @staticmethod
    @fresh_jwt_required
    def get():
        """
        Static method that fetches and returns all drones
        :return: a list of dicts with the drones data / an error message
        """
        drones = DroneModel.find_all_drones()
        if drones:
            output = []
            for drone in drones:
                output.append(process_cameras(drone))
            logging.info(output)
            return output
        logging.info("No drones found")
        return {
                   "message": "No drones found"
               }, 404


class DronesByName(Resource):
    @staticmethod
    @fresh_jwt_required
    def get():
        """
        Static method that fetches and returns all drones, sorted by name
        :return: a list of dicts with the drones data / an error message
        """
        drones = DroneModel.sort_drones_by_name()
        if drones:
            output = []
            for drone in drones:
                output.append(process_cameras(drone))
            logging.info(output)
            return output
        logging.info("No drones found")
        return {
                   "message": "No drones found"
               }, 404


class DronesBySerialnumber(Resource):
    @staticmethod
    @fresh_jwt_required
    def get():
        """
        Static method that fetches and returns all drones, sorted by serial number
        :return: a list of dicts with the drones data / an error message
        """
        drones = DroneModel.sort_drones_by_serialnumber()
        if drones:
            output = []
            for drone in drones:
                output.append(process_cameras(drone))
            logging.info(output)
            return output
        logging.info("No drones found")
        return {
                   "message": "No drones found"
               }, 404


class DroneRegister(Resource):

    @staticmethod
    @fresh_jwt_required
    def post():
        """
        Method saves a new drone.
        Can only be done if the user logged in is a support team user.
        :return: a success message / error message
        """
        user_team = UserModel.find_user_by_id(get_current_user()).team
        if user_team == 'Support':
            data = _drone_parser.parse_args()
            for camera in data['cameras'].split(','):
                found_camera = CameraModel.find_camera_by_model(camera.strip())
                if not found_camera:
                    logging.info("Camera not correct: {}".format(camera.strip()))
                    return {
                           "message": "Camera not correct: {}".format(camera.strip())
                       }, 400

            if DroneModel.find_drone_by_serial(data["serial_number"]):
                logging.info("Drone {} already exists".format(data["serial_number"]))
                return {
                           "message": "Drone {} already exists".format(data["serial_number"])
                       }, 400

            drone = DroneModel(data["serial_number"], data["name"], data["brand"], data['cameras'])
            drone.save_to_db()
            logging.info("Drone {} created".format(data["serial_number"]))
            return {
                "message": "Drone {} created".format(data["serial_number"])
            }
        else:
            logging.info("Non authorized user")
            return {
                       "message": "Non authorized user"
                   }, 400


def process_cameras(drone):
    """
    This method parses the drone "camera" field info and returns the drone with the found cameras data
    :param drone: the drone with just a string as cameras info
    :return: the drone with the cameras data assigned to it
    """
    drone = drone.json()
    cameras = []
    for camera in drone['cameras'].split(','):
        camera = camera.strip()
        found_camera = CameraModel.find_camera_by_model(camera)
        if found_camera:
            cameras.append(found_camera.json())
    drone['cameras'] = cameras
    return drone

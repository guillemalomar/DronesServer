import logging
import json
import requests

logging.basicConfig(filename='DataApp/logs/DataApp.log', level=logging.DEBUG)
logging.getLogger("urllib2").setLevel(logging.WARNING)


def get_users(hostname, port):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :return:
    """
    logging.debug('get_users method called')
    print("------------------ DATABASE USERS ------------------")
    r = requests.get("http://{}:{}/users".format(hostname, port))
    print(r.content.decode("utf-8"))


def get_drones(hostname, port):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :return:
    """
    logging.debug('get_drones method called')
    print("------------------ DATABASE DRONES ------------------")
    r = requests.get("http://{}:{}/drones".format(hostname, port))
    print(r.content.decode("utf-8"))


def get_cameras(hostname, port):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    """
    logging.debug('get_cameras method called')
    print("------------------ DATABASE CAMERAS ------------------")
    r = requests.get("http://{}:{}/cameras".format(hostname, port))
    print(r.content.decode("utf-8"))


def get_user_by_id(hostname, port, user_id):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param user_id: user id
    """
    logging.debug('get_user_by_id method called')
    print("------------------ DATABASE USERS ------------------")
    r = requests.get("http://{}:{}/user/{}".format(hostname, port, user_id))
    print(r.content.decode("utf-8"))


def get_drone_by_serialnumber(hostname, port, serial_number):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param serial_number: drone serial_number
    """
    logging.debug('get_drones_by_serialnumber method called')
    print("------------------ DATABASE DRONES ------------------")
    r = requests.get("http://{}:{}/drone/serial/{}".format(hostname, port, serial_number))
    print(r.content.decode("utf-8"))


def get_camera_by_model(hostname, port, model):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param model: camera model
    """
    logging.debug('get_cameras_by_model method called')
    print("------------------ DATABASE CAMERAS ------------------")
    r = requests.get("http://{}:{}/camera/{}".format(hostname, port, model))
    print(r.content.decode("utf-8"))


def sort_users_by_name(hostname, port):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :return:
    """
    logging.debug('sort_users_by_name method called')
    print("------------------ DATABASE USERS ------------------")
    r = requests.get("http://{}:{}/users/sort/name".format(hostname, port))
    print(r.content.decode("utf-8"))


def sort_drones_by_serialnumber(hostname, port):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :return:
    """
    logging.debug('sort_drones_by_serialnumber method called')
    print("------------------ DATABASE DRONES ------------------")
    r = requests.get("http://{}:{}/drones/sort/serialnumber".format(hostname, port))
    print(r.content.decode("utf-8"))


def sort_drones_by_name(hostname, port):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :return:
    """
    logging.debug('sort_drones_by_name method called')
    print("------------------ DATABASE DRONES ------------------")
    r = requests.get("http://{}:{}/drones/sort/name".format(hostname, port))
    print(r.content.decode("utf-8"))


def get_cameras_by_model(hostname, port):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    """
    logging.debug('get_cameras_by_model method called')
    print("------------------ DATABASE CAMERAS ------------------")
    r = requests.get("http://{}:{}/cameras/sort/model".format(hostname, port))
    print(r.content.decode("utf-8"))


def register_user(hostname, port, user, password, team):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param user:
    :type user:
    :param password:
    :type password:
    :param team:
    """
    logging.debug('register_user method called')
    print("------------------ REGISTERING USER ------------------")
    r = requests.post("http://{}:{}/user/register".format(hostname, port),
                      data={
                          'username': user,
                          'password': password,
                          'team': team
                      })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error trying to register the user")


def register_drone(hostname, port, serial_number, name, brand, cameras, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param serial_number:
    :type serial_number:
    :param name:
    :type name:
    :param brand:
    :type brand:
    :param cameras:
    :type cameras:
    :param access_token:
    :type access_token:
    """
    logging.debug('register_drone method called')
    print("------------------ REGISTERING DRONE ------------------")
    r = requests.post("http://{}:{}/drone/register".format(hostname, port),
                      data={
                          'serial_number': serial_number,
                          'name': name,
                          'brand': brand,
                          'cameras': cameras
                      },
                      headers={
                          'authorization': 'Bearer ' + access_token
                      })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error trying to register the drone")


def register_camera(hostname, port, model, megapixels, brand, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param model:
    :type model:
    :param megapixels:
    :type megapixels:
    :param brand:
    :type brand:
    :param access_token:
    :type access_token:
    :return:
    :rtype:
    """
    logging.debug('register_camera method called')
    print("------------------ REGISTERING CAMERA ------------------")
    r = requests.post("http://{}:{}/camera/register".format(hostname, port),
                      data={
                          'model': model,
                          'megapixels': megapixels,
                          'brand': brand
                      },
                      headers={
                          'authorization': 'Bearer ' + access_token
                      })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error trying to register the camera")


def delete_user(hostname, port, user_id, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param user_id: user id
    :param access_token:
    """
    logging.debug('delete_user method called')
    print("------------------ REGISTERING USER ------------------")
    r = requests.delete("http://{}:{}/user/{}".format(hostname, port, user_id),
                        headers={
                            'authorization': 'Bearer ' + access_token
                        })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error trying to delete the user")


def delete_drone(hostname, port, serial_number, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param serial_number: drone serial_number
    :param access_token:
    """
    logging.debug('delete_drone method called')
    print("------------------ REGISTERING DRONE ------------------")
    r = requests.delete("http://{}:{}/drone/serial/{}".format(hostname, port, serial_number),
                        headers={
                            'authorization': 'Bearer ' + access_token
                        })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error trying to delete the drone")


def delete_camera(hostname, port, model, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param model: camera model
    :param access_token:
    """
    logging.debug('delete_camera method called')
    print("------------------ DELETE CAMERA ------------------")
    r = requests.delete("http://{}:{}/camera/{}".format(hostname, port, model),
                        headers={
                            'authorization': 'Bearer ' + access_token
                        })
    if r.status_code == 200:
        print(json.loads(r.content.decode("utf-8"))['message'])
    else:
        print("Error trying to delete the camera")


def user_login(hostname, port, user, password):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param user:
    :type user:
    :param password:
    :type password:
    :return:
    :rtype:
    """
    logging.debug('register_camera method called')
    print("------------------ USER LOGIN ------------------")
    r = requests.post("http://{}:{}/login".format(hostname, port),
                      data={
                          'username': user,
                          'password': password
                      })
    print(json.loads(r.content))
    if r.status_code == 200:
        return json.loads(r.content.decode("utf-8"))['access_token']
    else:
        return None


def fill_database(hostname, port, access_token, data_file):

    with open(data_file) as json_file:
        data = json.load(json_file)
        r = None
        for camera in data['cameras']:
            r = requests.post("http://{}:{}/camera/register".format(hostname, port),
                              data={
                                  'model': camera['model'],
                                  'megapixels': camera['megapixels'],
                                  'brand': camera['brand']
                              },
                              headers={
                                  'authorization': 'Bearer ' + access_token
                              }
                              )
        if r:
            if r.status_code == 200:
                print("Cameras data loaded")
        else:
            print("Cameras data not loaded. Maybe you have to login first.")

    with open(data_file) as json_file:
        data = json.load(json_file)
        r = None
        for drone in data['drones']:
            r = requests.post("http://{}:{}/drone/register".format(hostname, port),
                              data={
                                  'serial_number': drone['serial_number'],
                                  'name': drone['name'],
                                  'brand': drone['brand'],
                                  'cameras': drone['cameras']},
                              headers={
                                  'authorization': 'Bearer ' + access_token
                              }
                              )
        if r:
            if r.status_code == 200:
                print("Drones data loaded")
        else:
            print("Drones data not loaded. Maybe you have to login first.")

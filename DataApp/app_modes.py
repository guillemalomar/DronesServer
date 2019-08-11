import logging
import json
import requests

logging.basicConfig(filename='DataApp/logs/DataApp.log', level=logging.INFO)
logging.getLogger("urllib2").setLevel(logging.INFO)


def get_users(hostname, port):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    """
    logging.debug('get_users method called')
    print("------------------ DATABASE USERS ------------------")
    r = requests.get("http://{}:{}/users".format(hostname, port))
    print(r.content.decode("utf-8"))


def get_drones(hostname, port, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param access_token: current user token
    """
    logging.debug('get_drones method called')
    print("------------------ DATABASE DRONES ------------------")
    r = requests.get("http://{}:{}/drones".format(hostname, port),
                     headers={
                         'authorization': 'Bearer ' + access_token
                     })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error obtaining the information. Is there information? Are you logged in?")


def get_cameras(hostname, port, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param access_token: current user token
    """
    logging.debug('get_cameras method called')
    print("------------------ DATABASE CAMERAS ------------------")
    r = requests.get("http://{}:{}/camera".format(hostname, port),
                     headers={
                         'authorization': 'Bearer ' + access_token
                     })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error obtaining the information. Is there information? Are you logged in?")


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


def get_drone_by_serialnumber(hostname, port, serial_number, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param serial_number: drone serial_number
    :param access_token: current user token
    """
    logging.debug('get_drones_by_serialnumber method called')
    print("------------------ DATABASE DRONES ------------------")
    r = requests.get("http://{}:{}/drone/serial/{}".format(hostname, port, serial_number),
                     headers={
                         'authorization': 'Bearer ' + access_token
                     })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error obtaining the information. Is there information? Are you logged in?")


def get_camera_by_model(hostname, port, model, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param model: camera model
    :param access_token: current user token
    """
    logging.debug('get_cameras_by_model method called')
    print("------------------ DATABASE CAMERAS ------------------")
    r = requests.get("http://{}:{}/camera/{}".format(hostname, port, model),
                     headers={
                         'authorization': 'Bearer ' + access_token
                     })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error obtaining the information. Is there information? Are you logged in?")


def sort_users_by_name(hostname, port):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    """
    logging.debug('sort_users_by_name method called')
    print("------------------ DATABASE USERS ------------------")
    r = requests.get("http://{}:{}/user/sort/name".format(hostname, port))
    print(r.content.decode("utf-8"))


def sort_drones_by_serialnumber(hostname, port, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param access_token: current user token
    """
    logging.debug('sort_drones_by_serialnumber method called')
    print("------------------ DATABASE DRONES ------------------")
    r = requests.get("http://{}:{}/drone/sort/serialnumber".format(hostname, port),
                     headers={
                         'authorization': 'Bearer ' + access_token
                     })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error obtaining the information. Is there information? Are you logged in?")


def sort_drones_by_name(hostname, port, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param access_token: current user token
    """
    logging.debug('sort_drones_by_name method called')
    print("------------------ DATABASE DRONES ------------------")
    r = requests.get("http://{}:{}/drone/sort/name".format(hostname, port),
                     headers={
                         'authorization': 'Bearer ' + access_token
                     })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error obtaining the information. Is there information? Are you logged in?")


def get_cameras_by_model(hostname, port, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param access_token: current user token
    """
    logging.debug('get_cameras_by_model method called')
    print("------------------ DATABASE CAMERAS ------------------")
    r = requests.get("http://{}:{}/camera/sort/model".format(hostname, port),
                     headers={
                         'authorization': 'Bearer ' + access_token
                     })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error obtaining the information. Is there information? Are you logged in?")


def register_user(hostname, port, user, password, team, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param user: user name
    :param password: user pass
    :param team: user team
    :param access_token: current user token
    """
    logging.debug('register_user method called')
    print("------------------ REGISTERING USER ------------------")
    r = requests.post("http://{}:{}/user/register".format(hostname, port),
                      data={
                          'username': user,
                          'password': password,
                          'team': team
                      },
                      headers={
                          'authorization': 'Bearer ' + access_token
                      })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error trying to register the user. Are you logged in as a Support user?")


def register_admin_user(hostname, port, user, password, team, secret_key):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param user: user name
    :param password: user pass
    :param team: user team
    :param secret_key: admin secret key
    """
    logging.debug('register_user method called')
    print("------------------ REGISTERING USER ------------------")
    r = requests.post("http://{}:{}/user/adminregister".format(hostname, port),
                      data={
                          'username': user,
                          'password': password,
                          'team': team,
                          'secret_key': secret_key
                      })
    if r.status_code == 200:
        print(r.content.decode("utf-8"))
    else:
        print("Error trying to register admin user. Are you using a correct key?")


def register_drone(hostname, port, serial_number, name, brand, cameras, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param serial_number: drone serial number (int)
    :param name: drone name
    :param brand: drone brand
    :param cameras: drone cameras
    :param access_token: current user token
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
        print("Error trying to register the drone. Are you logged in as a Support user?")


def register_camera(hostname, port, model, megapixels, brand, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param model: camera model
    :param megapixels: amount of megapixels
    :param brand: camera brand
    :param access_token: current user token
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
        print("Error trying to register the camera. Are you logged in as a Support user?")


def delete_user(hostname, port, user_id, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param user_id: user id
    :param access_token: current user token
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
        print("Error trying to delete the user. Are you logged in as a Support user?")


def delete_drone(hostname, port, serial_number, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param serial_number: drone serial_number
    :param access_token: current user token
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
        print("Error trying to delete the drone. Are you logged in as a Support user?")


def delete_camera(hostname, port, model, access_token):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param model: camera model
    :param access_token: current user token
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
        print("Error trying to delete the camera. Are you logged in as a Support user?")


def user_login(hostname, port, user, password):
    """
    Show the top10 pages, by points
    :param hostname: server location
    :param port: server port
    :param user: user name
    :param password: user pass
    :return: access token / None
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
        return g


def fill_database(hostname, port, access_token, data_file):
    """
    Obtains some test data and sends it to the server
    :param hostname: server location
    :param port: server port
    :param access_token: current user token
    :param data_file: file with test data
    """
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
            print("Cameras data not loaded. Maybe you have to login first as a Support member.")

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
            print("Drones data not loaded. Maybe you have to login first as a Support member.")

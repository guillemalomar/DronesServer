import argparse

from DataApp import app_modes
from DataApp.creds import ADMIN_SECRET_KEY

# Initial access token, wrong
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjUxNTU1MTksIm5iZiI6MTU2NTE1NTUxOSwianRpIjoiOTlkYzRlZjEtMjE0NS00ZGViLTg5NmUtNGZkMWY4YmFhMzhhIiwiZXhwIjoxNTY1MTU2NDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOnRydWUsInR5cGUiOiJhY2Nlc3MifQ.Mi_O3UvOolfG2OfgPKsYv_V3F-GM2FGEsaDmcEW1kHo"

admin_secret_key = ADMIN_SECRET_KEY


def clean_screen():
    """
    Method called to do a 'clear', just for application visualization purposes
    :return:
    """
    print(chr(27) + "[2J")


def message_header():
    """
    Print method for the header of the application
    :return:
    """
    print("******************************\n* Drones API Application *\n******************************")
    print("This is an application that accesses the Drones API to obtain or modify its data")


def show_modes():
    """
    Print method for the available data processing modes
    :return:
    """
    print("Available modes:")
    print("   1 - Get Users\n" +
          "   2 - Get Drones\n" +
          "   3 - Get Cameras\n" +
          "   4 - Get User by id\n" +
          "   5 - Get Drone by serial number\n" +
          "   6 - Get Camera by model\n" +
          "   7 - Sort Users by name\n" +
          "   8 - Sort Drones by serial number\n" +
          "   9 - Sort Drones by name\n" +
          "  10 - Sort Cameras by model\n" +
          "  11 - Register Ordinary User\n" +
          "  12 - Register Admin User\n" +
          "  13 - Register Drone\n" +
          "  14 - Register Camera\n" +
          "  15 - Delete User\n" +
          "  16 - Delete Drone\n" +
          "  17 - Delete Camera")


def message_output():
    """
    Print method for all the available modes
    :return:
    """
    show_modes()
    print(" ORDINARYLOGIN - Login as a normal user (needs to be registered first)\n" +
          " ADMINLOGIN    - Login as a support user (needs to be registered first)\n" +
          " LOAD          - Fill database with some data\n" +
          " HELP          - Show the initial application message\n" +
          " MODES         - Show the available modes\n" +
          " EXIT          - Quit application")


def check_input(input_var):
    """
    Method to check if the selected method is correct, and to exit if wanted
    :param input_var: user mode selected
    :return: True (Mode to execute) / False (Mode executed or incorrect)
    """
    if input_var.lower() == 'exit':
        print("The application will now end.")
        raise SystemExit
    elif input_var.lower() == 'modes':
        show_modes()
        return False
    elif input_var.lower() == 'help':
        message_output()
        return False
    elif input_var.lower() in ['load', 'ordinarylogin', 'adminlogin']:
        return True
    else:
        try:
            numeric_mode = int(input_var)
            if numeric_mode not in range(1, 18):
                print("Please enter a valid mode.")
                return False
        except ValueError:
            print("Please enter a valid mode.")
            return False
    return True


# Main method
if __name__ == "__main__":
    clean_screen()

    # Arguments are taken from command line
    parser = argparse.ArgumentParser(description='Drones API Client',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--hostname', action="store", dest="hostname",
                        help="Hostname to connect to the server",
                        default="localhost", type=str)
    parser.add_argument('--port', action="store", dest="port",
                        help="Port to connect to the server",
                        default=5000, type=int)
    parser.add_argument('--datafile', action="store", dest="datafile",
                        help="Datafile for the server database",
                        default='DataApp/test_data/my_data.json', type=str)

    args = parser.parse_args()
    hostname = args.hostname
    port = args.port
    data_file = args.datafile

    message_header()
    message_output()

    while True:
        correct_input = False
        var = None
        while not correct_input:
            print("***************************")
            var = input("Please, enter a new mode: ")
            correct_input = check_input(var)
        if var.lower() == 'load':
            app_modes.fill_database(hostname, port, access_token, data_file)
        if var.lower() == 'ordinarylogin':
            user = 'Tony'
            password = 'tonypass'
            access_token = app_modes.user_login(hostname, port, user, password)
        if var.lower() == 'adminlogin':
            user = 'Guillem'
            password = 'guillempass'
            access_token = app_modes.user_login(hostname, port, user, password)
        elif var == '1':
            app_modes.get_users(hostname, port)
        elif var == '2':
            app_modes.get_drones(hostname, port, access_token)
        elif var == '3':
            app_modes.get_cameras(hostname, port, access_token)
        elif var == '4':
            user_id = input("Please, en1ter a user id: ")
            app_modes.get_user_by_id(hostname, port, user_id)
        elif var == '5':
            serial_number = input("Please, enter a drone serial number: ")
            app_modes.get_drone_by_serialnumber(hostname, port, serial_number, access_token)
        elif var == '6':
            model = input("Please, enter a camera model: ")
            app_modes.get_camera_by_model(hostname, port, model, access_token)
        elif var == '7':
            app_modes.sort_users_by_name(hostname, port)
        elif var == '8':
            app_modes.sort_drones_by_serialnumber(hostname, port, access_token)
        elif var == '9':
            app_modes.sort_drones_by_name(hostname, port, access_token)
        elif var == '10':
            app_modes.get_cameras_by_model(hostname, port, access_token)
        elif var == '11':
            user = "Tony"
            password = "tonypass"
            team = "Development"
            app_modes.register_user(hostname, port, user, password, team, access_token)
        elif var == '12':
            user = "Guillem"
            password = "guillempass"
            team = "Support"
            secret_key = ADMIN_SECRET_KEY
            app_modes.register_admin_user(hostname, port, user, password, team, secret_key)
        elif var == '13':
            serial_number = input("Please, enter a drone serial number: ")
            name = input("Please, enter a drone name: ")
            brand = input("Please, enter a drone brand: ")
            cameras = input("Please, enter the drone cameras: ")
            app_modes.register_drone(hostname, port, serial_number, name, brand, cameras, access_token)
        elif var == '14':
            model = input("Please, enter a camera model: ")
            megapixels = input("Please, enter a number of megapixels: ")
            brand = input("Please, enter a brand: ")
            app_modes.register_camera(hostname, port, model, megapixels, brand, access_token)
        elif var == '15':
            user_id = input("Please, enter a user id: ")
            app_modes.delete_user(hostname, port, user_id, access_token)
        elif var == '16':
            serial_number = input("Please, enter a drone serial_number: ")
            app_modes.delete_drone(hostname, port, serial_number, access_token)
        elif var == '17':
            model = input("Please, enter a camera model: ")
            app_modes.delete_camera(hostname, port, model, access_token)

from DronesAPI.database.db import db


class DroneModel(db.Model):
    __tablename__ = "drones"
    serial_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    brand = db.Column(db.String(80))
    cameras = db.Column(db.String(80))

    def __init__(self, serial_number, name, brand, cameras):
        self.serial_number = serial_number
        self.name = name
        self.brand = brand
        self.cameras = cameras

    def json(self):
        """
        This method returns a dict containing the object data, to be returned easily
        """
        return {
            "serial_number": self.serial_number,
            "name": self.name,
            "brand": self.brand,
            "cameras": self.cameras
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
    def find_drone_by_serial(cls, serial_number):
        """
        Class method which finds user from DB by username
        :param serial_number: drone serial number
        :return: single db entry
        """
        return cls.query.filter_by(serial_number=serial_number).first()

    @classmethod
    def find_drone_by_name(cls, serial_number):
        """
        Class method which finds user from DB by username
        :param serial_number: drone serial number
        :return: single db entry
        """
        return cls.query.filter_by(serial_number=serial_number).first()

    @classmethod
    def find_all_drones(cls):
        """
        Class method which finds all drones from DB
        :return: list of db entries
        """
        return cls.query.all()

    @classmethod
    def sort_drones_by_name(cls):
        """
        Class method which finds all drones from DB and orders them by name
        :return: list of db entries
        """
        return cls.query.order_by("name").all()

    @classmethod
    def sort_drones_by_serialnumber(cls):
        """
        Class method which finds all drones from DB and orders them by serial number
        :return: list of db entries
        """
        return cls.query.order_by("serial_number").all()

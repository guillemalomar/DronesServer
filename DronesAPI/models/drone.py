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
        return {
            "serial_number": self.serial_number,
            "name": self.name,
            "brand": self.brand,
            "cameras": self.cameras
        }

    # Method to save user to DB
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Method to remove user from DB
    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    # Class method which finds user from DB by username
    @classmethod
    def find_drone_by_serial(cls, serial_number):
        return cls.query.filter_by(serial_number=serial_number).first()

    # Class method which finds user from DB by username
    @classmethod
    def find_drone_by_name(cls, serial_number):
        return cls.query.filter_by(serial_number=serial_number).first()

    # Class method which finds all drones from DB
    @classmethod
    def find_all_drones(cls):
        return cls.query.all()

    # Class method which finds all drones from DB and orders them by name
    @classmethod
    def sort_drones_by_name(cls):
        return cls.query.order_by("name").all()

    # Class method which finds all drones from DB and orders them by serial number
    @classmethod
    def sort_drones_by_serialnumber(cls):
        return cls.query.order_by("serial_number").all()

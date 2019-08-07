from DronesAPI.database.db import db


class CameraModel(db.Model):
    __tablename__ = "cameras"
    model = db.Column(db.String(80), primary_key=True)
    megapixels = db.Column(db.Float)
    brand = db.Column(db.String())

    def __init__(self, model, megapixels, brand):
        self.model = model
        self.megapixels = megapixels
        self.brand = brand

    def json(self):
        """
        This method returns a dict containing the object data, to be returned easily
        """
        return {
            "model": self.model,
            "megapixels": self.megapixels,
            "brand": self.brand
        }

    def save_to_db(self):
        """
        Method to save camera to DB
        """
        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        """
        Method to remove camera from DB
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_camera_by_model(cls, model):
        """
        Class method which finds camera from DB by model
        :param model: camera model
        :return: single db entry
        """
        return cls.query.filter_by(model=model).first()

    # Class method which finds all cameras from DB
    @classmethod
    def find_all_cameras(cls):
        """
        Class method which finds all cameras from DB
        :return: list of db entries
        """
        return cls.query.all()

    #
    @classmethod
    def sort_cameras_by_model(cls):
        """
        Class method which finds all cameras from DB and sorts them by model
        :return: list of db entries
        """
        return cls.query.order_by('model').all()

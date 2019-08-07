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
        return {
            "model": self.model,
            "megapixels": self.megapixels,
            "brand": self.brand
        }

    # Method to save camera to DB
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Method to remove camera from DB
    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    # Class method which finds camera from DB by model
    @classmethod
    def find_camera_by_model(cls, model):
        return cls.query.filter_by(model=model).first()

    # Class method which finds all cameras from DB
    @classmethod
    def find_all_cameras(cls):
        return cls.query.all()

    # Class method which finds all cameras from DB and sorts them by model
    @classmethod
    def sort_cameras_by_model(cls):
        return cls.query.order_by('model').all()

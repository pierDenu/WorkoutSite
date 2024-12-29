from app import db

class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def to_dict(cls):
        return {key: value for key, value in cls.__dict__.items() if not key.startswith('_')}


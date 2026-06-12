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

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


"""voivodesip model"""
from src import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# class Voivodeship(db.Model):
class Voivodeship(db.Base):
    "voivodeshiip table schema"
    __tablename__ = "voivodeships"

    voiv_id = Column(Integer, primary_key=True)
    voiv_name = Column(String(64), index=True, unique=True)
    # voiv_name = Column(String(64), index=True)
    terc = Column(Integer, unique=True)
    # terc = Column(Integer)
    unis = relationship("Uni", backref="voivodeships")

    def __init__(self, voivodeship: dict):
        self.voiv_name = voivodeship.get("voiv_name")
        self.terc = voivodeship.get("terc")

    # def json(self):
    #  return {'name':self.name,...}
    def __repr__(self):
        """
        String representation of the voivodeship.
        This representation is meant to be machine readable.
        :return: The voivodeship string.
        """
        return "<Voivodeship %r>" % (self.voiv_name)

    def __str__(self):
        """
        String representation of the voivodeship.
        This representation is meant to be human readable.
        :return: The voivodeship string.
        """
        return (
            f"Voivodeship: [voiv_id: {self.voiv_id}, "
            f"voiv_name: {self.voiv_name},terc:{self.terc}]"
        )

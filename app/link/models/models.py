from extensions import db
from dataclasses import dataclass


@dataclass
class Link(db.Model):
    """
    A Class containing link information

    """

    id: str = db.Column(db.String(150), primary_key=True)
    long_url: str = db.Column(db.String(255))
    short_url: str = db.Column(db.String(255))

    def __repr__(self):
        return f"<Link {self.id}>"

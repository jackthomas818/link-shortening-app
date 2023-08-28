import hashlib
import random
import string

from extensions import db
from link.models.models import Link


class LinkService:
    """
    A class responsible for generating shortened URLs from long URLs.
    """

    def generate_shorten_url(self, long_url, n_digits=8):
        """
        Generate a shortened URL for a given long URL.

        Args:
            long_url (str): The long URL to be shortened.
            n_digits (int, optional): The number of digits to use for the shortened URL code.
                                     Default is 8.

        Returns:
            Link: A Link instance containing the shortened URL.
        """

        if not long_url:
            raise ValueError("Long URL cannot be empty")

        # Get number of rows in database
        rows = db.session.query(Link).count()

        # Generate a base62 representation of the number of rows + 1 in the database
        code = self.encode(rows + 1)

        # Build the complete short URL using the generated code
        short_url = f"https://pa.ni/{code}"

        # Return a Link instance with the new information
        return Link(id=code, long_url=long_url, short_url=short_url)

    def save_link(self, Link):
        db.session.add(Link)
        db.session.commit()

    def encode(self, id):
        """
        Encodes an integer to a base62 representation
        """
        map = string.digits + string.ascii_letters
        encoding = ""
        # Convert Base-62
        while id > 0:
            p = id % 62
            encoding += map[p]
            id = id // 62
        return encoding

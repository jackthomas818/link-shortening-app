import hashlib
import random
import string

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

        # Generate a random alphanumeric (lower and upper case letters and numbers) string
        code = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(n_digits)
        )

        # Build the complete short URL using the generated code
        short_url = f"https://pa.ni/{code}"

        # Return a Link instance with the new information
        return Link(id=code, long_url=long_url, short_url=short_url)

    def save_link(self, Link):
        pass

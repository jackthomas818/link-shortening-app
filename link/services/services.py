import hashlib

from models.models import Link


class LinkService:
    def generate_shorten_url(self, long_url, n_digits=8):
        hash_object = hashlib.sha512(long_url.encode())

        code = hash_object.hexdigest()[0:n_digits]

        short_url = f"https://pa.ni/{code}"

        return Link(id=code, long_url=long_url, short_url=short_url)

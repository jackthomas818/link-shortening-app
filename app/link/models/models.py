class Link:
    """
    A Class containing link information

    """

    def __init__(self, id, long_url, short_url):
        """
        Initialize a Link instance

        Args:
            id (str): The unique identifier for the shortened URL.
            long_url (str): The original long URL.
            short_url (str): The generated shortened URL.

        """
        self.id = id
        self.long_url = long_url
        self.short_url = short_url

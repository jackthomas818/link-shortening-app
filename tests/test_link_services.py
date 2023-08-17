from link.services.services import LinkService


def test_generate_short_url():
    link_service = LinkService()
    long_url = "https://www.example.com/some/long/url"

    link = link_service.generate_shorten_url(long_url)

    assert link.id
    assert link.long_url == long_url
    assert link.short_url.startswith("https://pa.ni/")

from link.models.models import Link


def test_link_model():
    link = Link("abc12345", "https://www.example.com", "https://pa.ni/abc12345")

    assert link.id == "abc12345"
    assert link.long_url == "https://www.example.com"
    assert link.short_url == "https://pa.ni/abc12345"

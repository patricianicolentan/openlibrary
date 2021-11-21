"""
1. In one terminal window, run:
    * uvicorn main:app --reload
2. In a second terminal window, run:
    * source .venv/bin/activate
    * pip install pytest  # One time only.
    * python -m pytest

CAUTION: This test takes ~8 sec but may take up to a minute to complete!

TODO: Replace requests with an asyncio alternative such as httpx or trio...
https://anyio.readthedocs.io/en/stable/testing.html is installed by FastAPI.
"""
import requests

# url_base = "https://openlibrary.org"  # TODO: Tests to prove results are identical
url_base = "http://127.0.0.1:8000"
urls = """\
/docs
/redoc
/api/books?bibkeys=ISBN%3A0451526538%2CISBN%3A9780486280615
/api/volumes/brief/isbn/0450002314.json
/authors/OL34184A.json
/authors/OL23919A/works.json
/authors/OL23919A/works.json?limit=5
/books/OL7353617M
/isbn/9780140328721
/search.json?q=the+moon+is+a+harsh+mistress
/search.json?q=the+moon+is+a+harsh+mistress&page=2
/search/authors.json?q=arthur+c+clarke
/subjects/python.json
/subjects/python.json?details=True
/works/OL45883W
""".split()
# TODO: Add "/covers/isbn/0450002314-L.jpg"


# async def test_urls(urls: list[str] = urls):  # TODO
def test_urls(urls: list[str] = urls):
    for url in urls:
        response = requests.get(f"{url_base}{url}")
        assert response.status_code == 200, f"{url}: {response.status_code}"

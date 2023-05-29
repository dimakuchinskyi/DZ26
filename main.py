#1
class InvalidUrlError(Exception):
    def __init__(self, url):
        self.url = url
        super().__init__()

def fetch_data_from_url(url):
    try:
        if not is_valid_url(url):
            raise InvalidUrlError(url)
        return data
    except Exception as e:
        raise InvalidUrlError(url) from e
def is_valid_url(url):
    return True
url = "https://example.com"
try:
    fetch_data_from_url(url)
    print("Дані отримано успішно.")
except InvalidUrlError as e:
    print(f"Помилка при запиті URL: {e.url}")

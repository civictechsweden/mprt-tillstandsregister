from concurrent.futures import as_completed
from requests.adapters import HTTPAdapter
from requests_futures.sessions import FuturesSession
from urllib3.util import Retry

MAIN_URL = 'https://www.mprt.se/tillstandsregister/'
FETCH_MORE_URL = MAIN_URL + 'FetchMoreItems/?q=&page={}'

class Downloader(object):

    def __init__(self):
        adapter = HTTPAdapter(max_retries=Retry(total=10, backoff_factor=0.1))

        self.s = FuturesSession(max_workers=10)
        self.s.mount('https://', adapter)
        self.s.headers = {'Content-Type': 'text/xml;charset=UTF-8'}

    def fetch_tillstandsregister_homepage(self):
        return self.s.get(MAIN_URL).result().content

    def fetch_page(self, page):
        print(f'Fetching page {page}')
        future = self.s.get(FETCH_MORE_URL.format(page))
        future.page = page

        return future

    def fetch_pages(self, pages):
        futures = [self.fetch_page(page) for page in pages]

        i = 0
        for future in as_completed(futures):
            i += 1
            print(f'Fetched page {future.page} ({i}/{len(futures)})')

        return [future.result().content for future in futures]

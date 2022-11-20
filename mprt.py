from services.downloader import Downloader
from services.parser import Parser

def get_register_size(downloader=Downloader()):
    return Parser.parse_register_size(downloader.fetch_tillstandsregister_homepage())

def get_page(page, downloader=Downloader()):
    return Parser.parse_pages(downloader.fetch_page(page))

def get_pages(pages, downloader=Downloader()):
    return Parser.parse_pages(downloader.fetch_pages(pages))

def get_all_pages(downloader=Downloader()):
    size = get_register_size()
    nb_pages = size // 10 + 1
    pages = list(range(0, nb_pages + 1))

    return get_pages(pages, downloader)

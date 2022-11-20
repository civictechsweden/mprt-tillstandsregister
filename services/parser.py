from bs4 import BeautifulSoup

class Parser(object):
    @staticmethod
    def parse_register_size(response):
        soup = BeautifulSoup(response, 'html.parser')

        size = soup.select_one('div[class=content__wrapper] > strong > text').text.split(' ')[0]

        print(f'Found {size} items in the register.')

        return int(size)

    @staticmethod
    def parse_page(response):
        soup = BeautifulSoup(response, 'html.parser')
        trs = soup.select('tr')

        items = []

        for tr in trs:
            columns = tr.select_one('td').select('div > div > div > div[class*=col-18]')
            items.append({
                'name': Parser.__parse_column(columns[0]),
                'type': Parser.__parse_column(columns[1]),
                'owner': Parser.__parse_column(columns[2]),
                'publisher': Parser.__parse_column(columns[3]),
                'start': Parser.__parse_column(columns[4]),
                'end': Parser.__parse_column(columns[6]),
                'municipalities': Parser.__parse_column(columns[5]),
                'regions': Parser.__parse_column(columns[7])
            })

            print(f'Parsed {Parser.__parse_column(columns[0])}.')

        return items

    @staticmethod
    def parse_pages(responses):
        items = []
        for response in responses:
            items += Parser.parse_page(response)

        return items

    @staticmethod
    def __parse_column(column):
        bits = column.text.split('\n')

        if bits:
            return bits[4].strip()

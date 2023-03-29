import mprt
from services.writer import Writer

register = mprt.get_all_pages()
register = sorted(register, key=lambda d: d['name'])
register = sorted(register, key=lambda d: d['owner'])
register = sorted(register, key=lambda d: d['type'])

Writer.write_csv(register, 'register.csv')
Writer.write_json(register, 'register.json')

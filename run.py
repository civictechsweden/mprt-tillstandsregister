import mprt
from services.writer import Writer

register = mprt.get_all_pages()

Writer.write_csv(register, 'register.csv')
Writer.write_json(register, 'register.json')

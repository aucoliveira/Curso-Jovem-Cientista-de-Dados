# biblioteca regex expressões regulares

import re

palavra = r"Laura Maria da Silva\n(46) 93201-6392\n42010-7411\n(61) 47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell Technologies"
print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}|\d{5}\W\d{4}',palavra))

print('-='*50)
print()
palavra2 = r'contato@dellead.com, franciscojose@yahoo.com.br, ana.julia@universidade.edu, francisca-321-aline@meu-trabalho.net, Le@d Dell Technologies'

print(re.findall(r'[a-zA-Z0-9_.-]+@', palavra2))
print()
print(re.findall(r'@[a-zA-Z0-9-]+\.', palavra2))
print()
print()
print(re.findall(r'@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', palavra2))
print()
print(re.findall(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', palavra2))
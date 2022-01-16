from datetime import date, timedelta, datetime
import re

palavra =  '''2020-05-10 20:42:54,687 | INFO -> O programa foi iniciado
2020-05-11 00:09:52,532 | ERROR -> Erro não esperado
2020-05-11 09:01:10,812 | INFO -> O usuário utilizou o sistema
2020-05-11 19:06:13,609 | INFO -> O usuário utilizou o sistema
2020-05-11 20:46:35,271 | ERROR -> Erro não esperado
2020-05-12 08:14:59,895 | ERROR -> Erro não esperado
2020-05-12 11:33:59,700 | INFO -> O usuário utilizou o sistema
2020-05-13 10:20:14,673 | INFO -> O usuário utilizou o sistema
2020-05-13 16:58:10,298 | WARNING -> O usuário tentou fazer uma operação invalida
2020-05-14 03:55:25,383 | INFO -> O usuário utilizou o sistema
2020-05-15 02:59:29,002 | INFO -> O usuário utilizou o sistema
2020-05-15 08:40:33,776 | ERROR -> Erro não esperado
2020-05-15 13:45:29,089 | WARNING -> O usuário tentou fazer uma operação invalida
'''

#print(re.search(r'ERROR', palavra))
# ultilizando o '?' para procurar uma lista de caracteres específica

p = (re.findall(r'\d{4}\W\d{2}\W\d{2}\s\d{2}\W\d{2}\W\d{2}\W\d{3}\W+\|\s?ERROR\s\W\W\s[a-zA-Z0-9-].[a-zA-Z0-9-].+', palavra))
#hora = (re.findall(r'\d{}\W\d{}\W\d{}\s\d{2}\W\d{2}\W\d{2}\W\d{3}+', palavra))
#print(hora)
print('Existe(m)',len(p),'erro(s) no sistema', '\n',p)
print()

hora_erros = (re.findall(r'\s[0-9][0-9]\W[0-9][0-9]\W[0-9][0-9]\W[0-9][0-9][0-9]\W+\|\s?ERROR\s\W\W\s', palavra))
print(hora_erros)
print()
teste = hora_erros[0]
#print(len(teste))

#print((re.findall(r'\s[0-9][0-9]\W[0-9][0-9]\W[0-9][0-9]\W[0-9][0-9][0-9]\W',teste)))
#list_nova.append((re.findall(r'\s[0-9][0-9]\W[0-9][0-9]\W[0-9][0-9]\W[0-9][0-9][0-9]\W', list[i])))

def horas(list):
    list_nova = []
    for i in range(0, len(list)):
        list_nova.append((re.findall(r'\s[0-9][0-9]\W', list[i])))
    
    return list_nova

somente_horas = horas(hora_erros)

def conta_hora(list):
    for i in list:
        print('A hora ',i,' se repete ',list.count(i),' vezes.')

print('As horas que apresentam erro se repetem')
print(conta_hora(somente_horas))


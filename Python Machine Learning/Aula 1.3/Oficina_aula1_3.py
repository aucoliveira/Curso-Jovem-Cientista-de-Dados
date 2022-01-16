from datetime import date, timedelta, datetime
import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')

aniversarios = ['01/02/1990', '22 de Maio de 1991', '04/Abr/1995', '1995-Outubro-10', '12 Julho 1989', '16 de Junho de 1987', '04/07/1990']

aniversarios_novo =[]

data =aniversarios[1]
data2 = datetime.strptime(data,"%d de %B de %Y")
print(data2,type(data2))

for data in aniversarios:
    print(len(data))
    if len(data) <= 10:
        aniversarios_novo.append(datetime.strptime(data,"%d/%m/%Y"))
    elif len(data) > 10 and len(data) < 12:
        aniversarios_novo.append(datetime.strptime(data, "%d/%b/%Y"))
    elif len(data) > 12 and len(data) <= 14:
        aniversarios_novo.append(datetime.strptime(data, "%d %B %Y"))
    elif len(data) > 14 and len(data) <= 16:
        aniversarios_novo.append(datetime.strptime(data, "%Y-%B-%d"))
    else:
        aniversarios_novo.append(datetime.strptime(data, "%d de %B de %Y"))
    

print(aniversarios_novo)

aniversarios_lista_final = list(sorted(aniversarios_novo, key=lambda d: (d.month, d.day)))

print()
print(aniversarios_lista_final)

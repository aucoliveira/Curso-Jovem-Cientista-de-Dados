from datetime import date, timedelta, datetime
import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
hoje = date.today()

print(hoje)
print()
print(hoje.year)
print(hoje.month)
print(hoje.day)
print()

data_inicio = date(2021, 1, 25)
data_fim = date(2021, 5, 4)
print(f"O BBB 21 iniciou em {data_inicio} e terminou em {data_fim}")
print()
diferenca_dias = data_fim - data_inicio
duracao = diferenca_dias.days + 1
print(f'A duração do BBB 21 foi de {duracao} dias')
print()
hoje_novo = date(2021, 5, 14)
intervalo_dias = timedelta(days=28)
dia_futuro = hoje_novo + intervalo_dias
print(f'Daqui a 28 dias será {dia_futuro}')
print()

datas = [date(2016, 7, 6), date(2012, 10, 24), date(2020, 3, 19), date(2021, 8, 24), date(2021, 8, 12), date(2013, 5, 29), date(2018, 9, 2), date(2019, 1, 19), date(2012, 7, 2), date(2018, 9, 5)]
print(sorted(datas, key=lambda d: d.month))
print()
print(sorted(datas, key= lambda d: d.day))
print()
print(sorted(datas, key=lambda d: (d.month, d.day)))
print()
hoje_agora = datetime.now()
print(hoje_agora)
print()

# Criando uma lista com datas e horas para um alarme tocar
inicio = datetime(2021, 5, 24, 20, 30)
semana = [inicio]

for i in range(1, 7):
    dia_seguinte = inicio + timedelta(days=i)
    semana.append(dia_seguinte)

print(semana)
print()
def muda_horario(dia):
    if dia.weekday() == 1 or dia.weekday == 3:
        return dia.replace(hour=21)
    else:
        return dia

semana_atualizada = list(map(muda_horario, semana))

print(semana_atualizada)
print()

intervalo_dias = timedelta(weeks=12)
dia_futuro = hoje + intervalo_dias
diff = dia_futuro - hoje
days = diff.days
months, days = days // 30, days % 30
print(f'Desde {dia_futuro} passaram {months} meses e {days} dias')
print()
data_inicio = date(2021, 1 ,25)
print(data_inicio.strftime("%d/%m/%Y"))
print(data_inicio.strftime("%d %Y"))
print(data_inicio.strftime("%A %Y"))

print(data_inicio.strftime("%d de %B de %Y é uma %A"))
print()

data_inicio = date(2021, 1, 25)
print(data_inicio.strftime("%d/%m/%Y")) # 25/01/2021
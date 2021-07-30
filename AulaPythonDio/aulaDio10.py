from datetime import date, time, datetime, timedelta

def trabalhando_datime():
    data_atual=datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d %m %Y %H:%M:%S'))
    print((data_atual.strftime('%c')))
    print(data_atual.day)
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo ')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada.strftime('%c'))
    data_string = '1/1/2021'
    data_convertida = datetime.strptime(data_string, '%d/%m/%a')
    print(data_convertida)
    nova_data = data_atual - timedelta(days=365)
    print(nova_data)

def trabalhando_date():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H: %M: %S')
    print(horario_str)

if __name__ == '__main__':
    # data_atual =  date.today()
    # print(data_atual)
    # print(data_atual.strftime('%A %B %Y %d-%m-%y'))
    # trabalhando_date()
    trabalhando_datime()
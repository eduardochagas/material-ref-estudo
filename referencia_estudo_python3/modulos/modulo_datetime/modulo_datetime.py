
from datetime import date #para data do sistema
from datetime import datetime #para hora do sistema 

print('date.today() - retorna a data atual do sistema')
hoje = date.today()
print(hoje)
print()

print('date.today().day - retorna somente o dia da data do sistema.')
print('obs: o day É UMA PROPRIEDADE e não um método, por isso')
print('não tem parenteses no final da palavra')
dia = date.today().day
print('dia da data do sistema : dia %d' % dia)
print()

print('date.today().month - retorna somente o mês da data do sistema')
print('obs: o mês É UMA PROPRIEDADE e não um método, por isso')
print('não tem parenteses no final da palavra')
mes = date.today().month
print('mês da data do sistema: mês %d' % mes)
print()

print('date.today().month - retorna somente o ano da data do sistema')
print('obs: o ano É UMA PROPRIEDADE e não um método, por isso')
print('não tem parenteses no final da palavra')
ano = date.today().year
print('ano da data do sistema: ano %d' % ano)
print()

print('date.fromordinal(toordinal()+40) - determina a quantidade de')
print('dias após a data do dia atual do sistema.')
print('Daqui 40 dias será ', date.fromordinal(hoje.toordinal()+40))
print()

print('date.today().weekday() - retorna o número do dia da semana,')
print('começando em: 0 - segunda, 1 - terça, 2 - quarta... e assim por diante')
print('Dia da semana: ', hoje.weekday())
print()

# datetime
print('datetime.now().hour - retorna a hora agora do sistema')
print('obs: o hour É UMA PROPRIEDADE e não um método, por isso')
print('não tem parenteses no final da palavra')
horaagora = datetime.now()
hora = horaagora.hour
print('hora neste exato momento: %d horas' % hora)
print()

print('datetime.now().minute - retorna os minutos neste exato momento, do sistema.')
print('obs: o minute É UMA PROPRIEDADE e não um método, por isso')
print('não tem parenteses no final da palavra')
minutoagora = datetime.now()
minuto = minutoagora.minute
print('hora neste exato momento: %d minutos' % minuto)
print()

print('datetime.now().seconds - retorna os segundos neste exato momento do sistema')
print('obs: o seconds É UMA PROPRIEDADE e não um método, por isso')
print('não tem parenteses no final da palavra')
segundosagora = datetime.now()
segundos = segundosagora.second
print('hora neste exato momento: %d segundos' % segundos)
print()

print('')

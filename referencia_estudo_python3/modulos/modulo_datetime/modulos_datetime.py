'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# usando o modulo datetime (o modulo da datas)
#
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Metodos da Biblioteca Datetime.date
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

datetime.date(ano, mes, dia) - configura o ano, mês, dia do sistema.
datetime.date.min - 
datetime.date.max - 
datetime.date.resolution - 
datetime.date.year - retorna somente o ano da data.
datetime.date.month - retorna o mês do sistema em numero, entre o numero 1 e o numero 12 
datetime.date.day - retorna o dia do sistema entre 1 e o numero de dias em um dado mês (30 ou 31)
datetime.date.raplace(ano, mês, dia) - retorna a data com o mesmo valor configurado anteriormente,
 exeto se nesses parametros forem dados novos valores, aí a função troca os dados para os valores inseridos.

datetime.date.weekday() - retorna o dia da semana como um inteiro, onde  segunda (Monday) é 0 e
 domingo (Sunday) é 6, por exemplo, date(2002, 12, 4).weekday() == 2, uma quarta-feira (Wednesday).

datetime.date.ctime() - retorna uma string representando a data, 
 por exemplo: date(2002, 12, 4).ctime() == 'Wed Dec 4 00:00:00 2002'. d.ctime() é equivalente 
  á time.ctime(time.mktime(d.timetuple())) em plataformas onde a função ctime() nativa (qual é time.ctime() invoca,
 mas qual date.ctime() não invoca) conforme o padrão C.

datetime.date.strftime() - retorna a string representando a data, controlado por um formato explicito de string, ex:
  d.strftime('formato: %m/%d/%Y') #mostra a data configurada no formato string.

datetime.date.today() - mostra a data no formato ano-mês-dia, assim: 2017-11-02


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Metodos da Biblioteca Datetime.datetime()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

datetime.datetime(ano, mês, dia, hora, minuto, segundo, micro_segundo) - O ano, mês e dia são obrigatoriamente requeridos.
datetime.datetime.year - retorna o ano da data.
datetime.datetime.month - retorna o mês da data.
datetime.datetime.day - retorna o dia da data.
datetime.datetime.hour - retorna a hora da data.
datetime.datetime.minute - retorna os minutos da data.
datetime.datetime.second - retorna os segundos da data.
datetime.datetime.today() - retorna a data do dia, mês, ano e a as horas (hora, min, seg).
datetime.datetime.date() - retorna somente as datas: ano, mês, dia.
datetime.datetime.ctime() - retorna o nome do dia, o nome do mês, o numero do dia, as horas, min, seg e o ano (nessa ordem), 
 ex: 'Thu Nov  2 15:31:00 2017'
datetime.datetime.timetuple() - retorna o ano, mês, dia, hora, min, seg, dia_da_semana, dia_do_ano, assim,
 ex: (tm_year=2017, tm_mon=11, tm_mday=2, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=306, tm_isdst=-1)






# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Metodos da Biblioteca Datetime.datetime.now()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


OBS: nomes que são propriedades do datetime.now(): month, day, year, hour, minute e second 
 
datetime.datetime.now() - 
datetime.datetime.now().month - mostra somente o mês.
datetime.datetime.now().day - mostra somente o dia.
datetime.datetime.now().year - mostra somente o ano.
datetime.datetime.now().hour - mostra somente a hora 
datetime.datetime.now().minute - mostra somente o minuto.
datetime.datetime.now().second -  mostra somente o segundo.

'''



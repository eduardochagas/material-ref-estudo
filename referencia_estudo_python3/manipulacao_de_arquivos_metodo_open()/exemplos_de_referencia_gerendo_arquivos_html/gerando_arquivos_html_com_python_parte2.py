
pagina = open('pagina2.html', 'w', encoding='utf-8')
pagina.write('<!DOCTYPE HTML>\n')
pagina.write('<html lang="pt-br">\n')
pagina.write(' <head> \n')
pagina.write('       <title>Professor Neri - html5</title>\n')
pagina.write(' </head>\n ')
pagina.write(' <body>\n  ')
pagina.write('     <h1>Video aulas Neri</h1><br/>\n ')
#pagina.write('         7 * 1 = 7<br>\n ')
#pagina.write('         7 * 2 = 14<br>\n ')
#pagina.write('         7 * 3 = 21<br>\n ')
#pagina.write('         7 * 4 = 28<br>\n ')
#pagina.write('         7 * 5 = 35<br>\n ')
#pagina.write('         7 * 6 = 42<br>\n ')
#pagina.write('         7 * 7 = 49<br>\n ')
#pagina.write('         7 * 8 = 56<br>\n ')
#pagina.write('         7 * 9 = 63<br>\n ')

# Faça linha a linha conforme acima ou faça usando for como abaixo.
for tabuada in range(1,11):
    pagina.write('9 x %d = %d <br/> \n' % (tabuada, 9*tabuada))


pagina.write('         <br>Prof Neri Aldoir Neitzke\n')
pagina.write(' </body>\n')
pagina.write('</html>\n')
pagina.flush()
pagina.close()

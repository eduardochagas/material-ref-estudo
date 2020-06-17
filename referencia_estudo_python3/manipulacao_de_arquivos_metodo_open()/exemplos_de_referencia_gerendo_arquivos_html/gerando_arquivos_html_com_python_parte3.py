
pagina = open('pagina3.html', 'w', encoding='utf-8')
pagina.write('''<!DOCTYPE HTML>
<html lang="pt-br">
 <head> 
       <title>Professor Neri - html5</title>
 </head>
 <body>
     <h1>Video aulas Neri</h1><br/> 
''')
for tabuada in range(1,11):
    pagina.write('9 x %d = %d <br/>' % (tabuada, 9*tabuada))

pagina.write('''         <br>Prof Neri Aldoir Neitzke
 </body>
</html>
''')

pagina.flush()
pagina.close()

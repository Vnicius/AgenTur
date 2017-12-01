'''
    Gerar base de dados aleatoriamente
'''
from random import randint

for rota in range(18):
    out = open(str(rota)+'.csv', 'w')
    for dia in range(0,7):
        for hora in range(0,24):
            fluxo = 0
            espera = 0

            if int(hora/6) == 0:
                fluxo = randint(1, 3)
                espera = randint(0, 2)

            elif  int(hora/6) == 1:
                fluxo = randint(3, 8)
                espera = randint(1, 10)

            elif int(hora/6) == 2:
                fluxo = randint(5, 15)
                espera = randint(8, 20)
            else:
                fluxo = randint(2, 10)
                espera = randint(2, 15)

            el = [str(dia),str(hora),str(fluxo),str(espera)]
            #row.append(el)
            out.write(','.join(el) + "\n")
        #print(row)
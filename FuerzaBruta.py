from string import ascii_letters , digits
from itertools import product
caracteres=ascii_letters+digits
def buscador(con):
    archivo =open("combinaciones.txt","w")
    if 3<= len(con)<=4:
        for i in range(3,5):
            for comb in product(caracteres, repeat=i):
                prueba="".join(comb)
                archivo.write(prueba + "\n")
                if prueba== con:
                    print("tu contraseña es {}".format(prueba))
                    archivo.close()
                    break
    else:
        print('ingrese una contraseña de 3 a 4 caracteres')

from time import time
t0=time()
con='H0l4'
buscador(con)
print('tiempos de ejecucion {}'.format(round(time()-t0,6)))

memoria = [1:0, 2:1, 3:1]
def fibonacci_top_down(numero):
    if numero in memoria:
        return memoria[numero]
    f=fibonacci_iterativo_v2(numero-1)+fibonacci_iterativo_v2(numero-2)
    memoria[numero]=f
    return memoria[numero]
fibonacci_top_down(12)
memoria
fibonacci_top_down(8)
memoria

import pickle
archivo=open('memoria.py','wb')
pickle.dump(memoria, archivo)
archivo.close()

archivo=open('memoria.p','rb')
memoria_de_archivo=pickle.load(archivo)
archivo.close()
memoria
memoria_de_archivo

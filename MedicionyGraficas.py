%pylab inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import random
from time import time
from insertionSort import insertionSort_time
from quickSort import quicksort_time

datos=[ii*100 for ii in range(1,21)]
tiempo_is=[]
tiempo_qs=[]
for ii in datos:
    lista_is=random.sample(range(0, 10000000), ii)
    lista_qs=lista_is.copy()
    t0=time()
    insertionSort_time(lista_is)
    tiempo_is.append(round(time()-t0, 6))
    
    t0=time()
    quicksort_time(lista_qs)
    tiempo_qs.append(round(time()-t0, 6))
print('Tiempos parciales de ejecucion en INSERT SORT {} [s]\n'.format(tiempo_is))
print('Tiempos parciales de ejecucion en QUICK SORT {} [s]'.format(tiempo_qs))
print('Tiempos total de ejecucion en insert sort {} [s]'.format(sum(tiempo_is)))
print('Tiempos total de ejecucion en quick sort {} [s]'.format(sum(tiempo_qs)))
fig, ax=subplots()
ax.plot(datos, tiempo_is, label='insert sort', marker='*',color='r')
ax.plot(datos, tiempo_qs, label='quick sort', marker='°',color='b')
ax.set_xlabel('Datos')
ax.set_ylabel('Tiempo')
ax.grid(True)
ax.legend(loc=2);

plt.title('Tiempo de ejecucion [s] (insert vs. quick)')
plt.show()


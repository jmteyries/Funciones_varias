# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:51:06 2021

@author: jtintore
"""


from datetime import datetime, timedelta
import numpy as np



#Esta funcion saca los dias festivos que hay entre las dos fechas 

def laboral(begin, end):
    # en el caso de que begin y end esten en otro formato habra que cambiarlo 
    # en estadocasos se utiizaron estos formatos: '%d/%m/%Y %H:%M:%S +00:00' y '%m/%d/%Y %I:%M:%S %p +00:00'

    inicio=np.array(begin + timedelta(days=0),'datetime64[D]')
    final=np.array((end + timedelta(days=1) - timedelta(days=0)) ,'datetime64[D]') # le sumamos uno dia ya que la end date no la inlcuye en el recuento
    dias_laborables_total= np.busday_count(inicio,final)-2
    
    if dias_laborables_total<0:
        dias_laborables=0
    else:
        dias_laborables=dias_laborables_total

    return dias_laborables


def laboral_hora(begin,end):
    # delta son los dias laborales enteros de 8 horas
    # primero a string y solo cogemos la hora
    delta= laboral(begin, end)
    
    aa=begin.weekday() # lunes seria 0 sabado 5 domingo 6
    zz=end.weekday()
    
    delta_horas=delta*timedelta(hours=8, minutes=0, seconds=0)
    inicio=datetime.strftime(begin, '%H:%M:%S')
    dia_inicio=datetime.strftime(begin, '%d/%m/%Y')
    
    final=datetime.strftime(end, '%H:%M:%S')
    dia_final=datetime.strftime(end, '%d/%m/%Y')
    
    inicio_jornada=datetime.strptime('08:00:00', '%H:%M:%S')
    final_jornada=datetime.strptime('18:00:00', '%H:%M:%S')
    # ahora a datetime
    inicio_ticket=datetime.strptime(inicio,'%H:%M:%S')
    final_ticket=datetime.strptime(final,'%H:%M:%S')
    
    # hacemos condicionaes para ver si el inicio y el final estan dentro la jornada
    if final_jornada > inicio_ticket > inicio_jornada:
        comienza= inicio_ticket
    elif final_jornada > inicio_ticket < inicio_jornada:
        comienza=inicio_jornada
    else:
        comienza=0
    
    if final_jornada > final_ticket > inicio_jornada:
        finaliza=final_ticket
    elif final_jornada < final_ticket > inicio_jornada:
        finaliza=final_jornada
    else:
        finaliza=0
    
    
    if delta != 0 or delta==0 and dia_final!=dia_inicio: 
        # el inicio_ticket y final_ticket estan en dias distintos
        # construimos las operaciones con casuisticas
        if comienza != 0:
            if aa<5:
                operacion_inicio= final_jornada-comienza
            else:
                operacion_inicio= timedelta(hours=8, minutes=0, seconds=0)
        else:
            operacion_inicio= timedelta(hours=0, minutes=0, seconds=0)
       
        if finaliza != 0:
            if zz<5: 
                operacion_final= finaliza - inicio_jornada
            else:
                operacion_final= timedelta(hours=8, minutes=0, seconds=0)
        else:
            operacion_final= timedelta(hours=0, minutes=0, seconds=0)
        
        tiempo_restante= operacion_final + operacion_inicio
        
    else:
        tiempo_restante= finaliza - comienza
    
    
    #tiempo_restante= (final_jornada-inicio_ticket) + (final_ticket-inicio_jornada)
    
    tiempo_total= delta_horas + tiempo_restante
    
    
    return tiempo_total


a='12/02/2021 10:09:06'
b='27/02/2021 18:32:02'



c='28/01/2021 10:49:00'
d='28/01/2021 21:15:00'

a_real=datetime.strptime(a, '%d/%m/%Y %H:%M:%S')
b_real=datetime.strptime(b, '%d/%m/%Y %H:%M:%S')

a_dia=datetime.strptime('14/02/2021', '%d/%m/%Y')
b_dia=datetime.strptime('27/02/2021', '%d/%m/%Y')

print(b_real.weekday())

c_real=datetime.strptime(c, '%d/%m/%Y %H:%M:%S')
d_real=datetime.strptime(d, '%d/%m/%Y %H:%M:%S')
c_dia=datetime.strptime('11/02/2021', '%d/%m/%Y')
d_dia=datetime.strptime('27/01/2021', '%d/%m/%Y')

b_real_real=datetime.strftime(b_real, '%m/%d/%Y %I:%M:%S %p')
print(b_real_real)

aj=laboral(a_real,b_real)
print (laboral(a_real,b_real))
print(laboral_hora(a_real,b_real))
print(type(aj))

d=1*timedelta(hours=8, minutes=0, seconds=0)
print (d)
print((laboral_hora(a_real,b_real)-d))
print('·········/////////////···············')
print (laboral(c_real,d_real))
print(laboral_hora(c_real,d_real))

festivos=[]
festivos.append(a_dia)
festivos.append(b_dia)
festivos.append(c_dia)
festivos.append(d_dia)


cars=np.array(festivos,'datetime64[D]')

i=datetime.strptime('11/02/2021', '%d/%m/%Y')

i_array=np.array(i,'datetime64[D]')
if i_array in cars:
    print('oleeee esta dentro')
else:
    print('Juanito vuelve a mirarlo')


import numpy as np


t1 = 90
t2 = -30


x = 140*np.cos((t1+t2)*(np.pi/180)) + 174*np.cos((t1)*(np.pi/180))
y = 140*np.sin((t1+t2)*(np.pi/180)) + 174*np.sin((t1)*(np.pi/180))

x = round(x, 1)
y = round(y, 1)
################################33
print ("x", x)
print ("y", y)
#x = 233
#y = 180


#assumindo compilação correta e o ponto esta na área de trabalho
#primeiro o segundo angulo
t2n = np.arccos((pow(x,2)+ pow(y,2) - pow(174,2) - pow(140,2)) / (2*140*174))

k = 0
if y<0:
    t2n = abs(t2n)
    k = 1
    y = abs(y)

#calculo um valor possível para teta1 e testo para saber se é válido
num = y*(174+140*np.cos(t2n) )  - x*140*np.sin(t2n)
den = x*(174+140*np.cos(t2n) )  + y*140*np.sin(t2n)

t1n = np.arctan(num/(den+0.0001)) #aproximação para evitar divisão por zero.

if k==1:
    t1n = abs(t1n)
    t2n = -abs(t2n)
    

print (".....")
print ("tn1", round(t1n*(180/np.pi), 0))
print ("tn2", round(t2n*(180/np.pi), 0))


x = 140*np.cos(t1n+t2n)+174*np.cos(t1n)
y = 140*np.sin(t1n+t2n)+174*np.sin(t1n)

x = round(x, 1)
y = round(y, 1)

print (".....")
print ("xn", x)
print ("yn", y)

        #coloco em posição
        #ylinha = 140*np.sin((t1n+t2n)*(np.pi/180))+174*np.sin((t1n)*(np.pi/180))
        
        #braço virado para baixo
        #if y < ylinha:
         #   t2n = -abs(t2n)
          #  num = y*(174+140*np.cos(t2n) )  - x*140*np.sin(t2n)
           # den = x*(174+140*np.cos(t2n) )  + y*140*np.sin(t2n)

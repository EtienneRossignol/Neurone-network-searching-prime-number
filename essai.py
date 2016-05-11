# Créé par Etienne, le 06/05/2016 en Python 3.2
from neurones import Reseau
from random import randint


TMAX=100
L=[True]*TMAX
for i in range(2,TMAX):
    if L[i]:
        for el in range(i**2,TMAX,i):
            L[el]=False
test=[]
exemple=[]
val=0
for i in range(2,TMAX):
    if L[i]:
        val+=1
        if randint(0,2)!=0:
            exemple.append(([val],[i/5000]))
        else:
            test.append(([val],[i/5000]))

r=Reseau(1,20,20,1)
minmimum=1000*1000*1000
machin=[]
for i in range(500000):
    #for entre,sortie in exemple:
    #    r.retropropogationDuGradient(entre,sortie)
    r.apprentissageExemple(exemple)
    valeur=0
    for entre, sortie in test:
        valeur+=(r.calculerSortie(entre)[0]-sortie[0])**2
    if valeur<minmimum:
        minmimum=valeur
        machin=[[[r.poid[a][b][c] for c in range(r.arg[a+1])]
           for b in range (r.arg[a]+1)]for a in range(len(r.arg)-1)]
        #for i in range(200):
         #   print(r.calculerSortie([i]))
        print(minmimum*5000*5000)
        print("-"*10)
    if i%10==0:
        print(i)
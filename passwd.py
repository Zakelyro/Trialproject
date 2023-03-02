# -*- coding: utf-8 -*-
"""
Spyder Editor

Random Password generator
"""
import random 

# Password making T1 
# T1==4 letters and encoding
L1=['Gauv','Isei','Geas','Dick','Cock','Lugh','KenK','KIRA','IITB','IITK','Porn','Solo','Abys','Sieg','Lily','Jack','Jily','Mark','Fuck','Fate','Zero','Lelu','Time','Dura','IDFC','Doge','Elon','Plat','Phil','BioB','LilG','Tore','Pika','Char','GenG','Giga','Pyro','Heal','Stay','DESE','IITD','IITM','MEMS','ESED','DSAI','Rose','Lily','Wing','Skye','Sing','ABCD','Zest','Test','CGPA','UGPG','Coke','Math','Segs','Dang','Fang','Wolf','Homi','MITA','JSPM','AIDS','Wayn','XLR8','Kiyo']
L2=['!','@','#','$','%','^','&','*','>','<','?','/']
print(len(L1))
#random.choice(L1)
#random.shuffle(L2)
#random.randint(a,b) gives an int b/w a and b 

 # for i in L1:
   # if L1.index(i)==7:
    #    for j in i:
     #       a.append(j)
      #      a.append(' ')
def getdigits(La):
    a=[]
    b=[]
    for i in La:
       a.append(ord(i))
    for i in a:
        b.append(str(i % 10))
    return b
#print(getdigits('IITB'))

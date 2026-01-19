#Stampa tutti i numeri da 1 a 100
#per i multipli di 3 stampa ZUM
#per i multipli di 5 stampa BUM
#per i multipli di 3 E 5 stampa BANGARANG

for i in range (1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("BANGARANG")
  elif i % 3 == 0:
    print("ZUM")
  elif i % 5 == 0:
    print("BUM")
  else:
    print(i)
    

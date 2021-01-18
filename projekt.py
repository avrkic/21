import random
#Karte
 #Dilerove karte
dilerove_karte = []
 #Igraceve karte
igraceve_karte = []

# Risavanje dijeljena karata i pokazivanja istih
#Za sada gledamo osnovne karte kao bodove (poslije spil i brojevi, zogovi...)

#Dilerove karte
while len(dilerove_karte) != 2:
  dilerove_karte.append(random.randint(1,11))
  if len(dilerove_karte) == 2:
    print("Diler ima jednu neotkrivenu kartu i ",dilerove_karte[1])
    
#Igraceve karte
while len(igraceve_karte) != 2:
  igraceve_karte.append(random.randint(1,11))
  if len(igraceve_karte) == 2:
    print("Imate karte: ",igraceve_karte)
    
#Zbrajam dilerove karte
if sum(dilerove_karte) == 21:
  print("Diler ima blackjack izgubili ste!")
elif sum(dilerove_karte) > 21:
  print("Diler je bust, pobjedili ste!")
  
#Zbrajam igraceve karte i njegov potez  

while sum(igraceve_karte < 21):
  ispis = str(input("Stay or Hit"))
  if ispis == "Hit":
    igraceve_karte.append(random.randint(1,11))
    print("Imate: " + str(sum(igraceve_karte)) + " sa kartama: ",igraceve_karte)
  else:
    print("Diler ima: " + str(sum(dilerove_karte)) + " sa kartama: ",dilerove_karte)
    print("Imate: " + str(sum(igraceve_karte)) + " sa kartama: ",igraceve_karte)
    if sum(dilerove_karte) > sum(igraceve_karte):
      print("Kuca pobjeduje!")
    elif sum(igraceve_karte) == sum(dilerove_karte):
      print("Push! Ulozi vam se vračaju.")
     else:
      print("Dobili ste!")
      break
      
#Zadnje provjere

if sum (igraceve_karte) > 21:
  print("Bust! Izgubili ste.")
elif sum(igraceve_karte) == 21:
  print("Imate BlackJack! Dobili ste.")


print("Měříš 175 cm.")
vyska = 175
print("Vážíš 77 kg. ")
vaha = 77
print("Jsi Jakub. ")
jmeno = "Jakub"
bmi = ((vaha /100)/ (vyska ** 2))
kategorie = None
if bmi < 25:
  kategorie = "Podvýživa" if bmi < 18.5 else "Zdravá váha"
elif bmi > 30:
  kategorie = "Těžká obezita" if bmi > 40 else  "Obezita"
else:
  kategorie = "Mírná nadváha"

print("Jméno: ",jmeno,", kategorie: ",kategorie)
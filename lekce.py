text = "indexování"

print("Prvních 5 písmen:\n", text[:5],"\nPosledních 5 písmen:\n", text[-5:],"\nKaždé třetí písmeno (počínaje prvním) od 'i':\n", text[::3])

kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

kg_pocet = 80
km_pocet = 54
l_pocet = 5

kg_vysledek = kg_pocet * kg_lb
km_vysledek = km_pocet * km_mile
l_vysledek = l_pocet * l_gal

print("80 kg je", kg_vysledek, "liber, \n54 km je", km_vysledek, "mil \n5 litrů je", l_vysledek, "galonů.")

mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

sleva_merc = 5000
cena_2_merc = mercedes * 2
cena_merc_a_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou = (rolls_royce + vybava) * 2
cena_merc_s_vybavou = mercedes + vybava
merc_se_slevou = mercedes - sleva_merc

print("Sleva na Mercedes:", sleva_merc, "\nCena za dva Mercedesy je:", cena_2_merc, "\nCena za Mercedes a Rolls-Royce:", cena_merc_a_rolls, "\nCena za dva Rolls-Royce s příplatkovou výbavou:", cena_2_rolls_s_vybavou, "\nCena za Mercedes s příplatkovou výbavou:", cena_merc_s_vybavou, "\nCena za Mercedes po slevě:", merc_se_slevou)

jmeno = "Lukáš"
prijmeni = "Dvořák"
cele_jmeno = jmeno + " " + prijmeni
delka_jmena = len(cele_jmeno)

print("Celé jméno: ",cele_jmeno,"\nDélka jména: ",delka_jmena,"\n","="*delka_jmena,"\n",cele_jmeno,"\n","="*delka_jmena)

cislo_1 = float(input("napiš první číslo: "))
cislo_2 = float(input("napiš druhý číslo: "))
if cislo_1 > cislo_2:
    print("První číslo je větší než druhé.")
elif cislo_1 < cislo_2:
    print("Druhé číslo je větší než první.")
else:
    print("Čísla jsou stejná.")



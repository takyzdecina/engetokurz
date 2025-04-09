slovnik = dict()
slovnik = {"jmeno" : "jakub","vek" : 20, "vyska" : 175, "vaha" : 77, 
        "zájmy": ["programování","sport","cestování"], 
        "kontakt":("adresa","telefon"),
        "mesta":{"praha":"nuda","brno":"zábava","olomouc":"pohoda"},
        "auto":None,}
print(type(slovnik))
print(slovnik)
print(slovnik["jmeno"],slovnik["vyska"])
print(slovnik.items())
print(slovnik["vek"])
print(slovnik.setdefault("krmeni","zrno"))
novy = slovnik.fromkeys(["jmeno", "vek", "vyska", "vaha"])
print(novy)
print(slovnik.get("vek"))
print(slovnik.pop("vaha"))
print(slovnik["zájmy"][1])
print(slovnik["mesta"]["praha"])
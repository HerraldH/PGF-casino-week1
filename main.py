print("-----------------------------------------------------")
print("Casino de Gouden Driehoek")
print("-----------------------------------------------------")
print("Vul uw Gegevens in")
voornaam = input("Voornaam: ")
tussenvoegsel = input("Tussenvoegsel: ")
achternaam = input("Achternaam: ")
voornaam = voornaam.capitalize()
achternaam = achternaam.capitalize()
tussenvoegsel = tussenvoegsel.lower()
if tussenvoegsel != "":
    volledige_naam = f"{voornaam} {tussenvoegsel} {achternaam}"
elif tussenvoegsel == "":
    volledige_naam = f"{voornaam} {achternaam}"
print("-----------------------------------------------------")
print(f"Hallo {volledige_naam}.")
print("Wat is uw geboortedatum?")
geboortedatum = input("[dd-mm-yyyy]: ")
if len(geboortedatum) != 10:
    print("Ongeldig format")
dag = float(geboortedatum[:2])
maand = float(geboortedatum[3:5])
jaar = float(geboortedatum[6:])
if dag <1 or dag >31:
    print("Ongeldig format")
if maand <1 or maand >12:
    print("Ongeldig format")
if maand == 1:
    maand = "januari"
elif maand == 2:
    maand = "februari"
elif maand == 3:
    maand = "maart"
elif maand == 4:
    maand = "april"
elif maand == 5:
    maand = "mei"
elif maand == 6:
    maand = "juni"
elif maand == 7:
    maand = "juli"
elif maand == 8:
    maand = "augustus"
elif maand == 9:
    maand = "oktober"
elif maand == 10:
    maand = "september"
elif maand == 11:
    maand = "november"
elif maand == 12:
    maand = "december"
geboortedatum_check = f"{int(dag)} {str(maand)} {int(jaar)}"
print(f"Is uw geboorte datum: {geboortedatum_check}?")
input("[Typ ['Y' voor akkoord] & ['N' voor niet akkoord]: ")
print("-----------------------------------------------------")
print("Wat is uw geslacht?")
geslacht = input("[man, vrouw]: ")
print("-----------------------------------------------------")
if geslacht == "man" or geslacht == "Man":
    aanspreking_woord = "meneer"
elif geslacht == "vrouw" or geslacht == "Vrouw":
    aanspreking_woord = "mevrouw"
else:
    aanspreking_woord = f" {str(voornaam[:1])}."
print(f"Welkom {aanspreking_woord} {achternaam}")
print("Wat is uw budget voor vandaag?")
budget = input("Budget: €")
tt = "14.99"
vd = " 3.99"
gb = " 0.99"
t = float(tt) + float(vd) + float(gb)
print(" ")
print(" ")
print(" ")
print("-----------------------------------------------------")
print("Casino de Gouden Driehoek")
print("-----------------------------------------------------")
print(f"Welkom, {aanspreking_woord} {achternaam}")
print("Bij Casino DGD hanteren wij de volgende vaste kosten.")
print("-----------------------------------------------------")
print(f"Toegangsticket:                               € {tt}")
print(f"Één verplicht drankje:                        € {vd}")
print(f"Gok belasting:                                € {gb}")
print(" ")
print(f"Totaal:                                       € {t} ")
print("-----------------------------------------------------")
print(" ")
print("Gaat u hier mee akkoord?")
akkoord_vaste_kosten = input("Typ ['Y' voor akkoord] & ['N' voor niet akkoord]: ")
if akkoord_vaste_kosten == "Y" or akkoord_vaste_kosten == "y":
    print(" ")
else:
    print("Niet akkoord")
if float(budget) < float(t):
    print(" Uw budget voor vandaag is te weinig.")
    print("Fijne dag verder.")
else:
    print(" ")
    print(" ")
    print(" ")
    print("-----------------------------------------------------")
    print("Casino de Gouden Driehoek")
    print("-----------------------------------------------------")
    print(f"Welkom, {aanspreking_woord} {achternaam}")
    print(f"Uw budget voor vandaag is €{float(budget) - float(t)}")
    print("-----------------------------------------------------")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("-----------------------------------------------------")
    print(" ")

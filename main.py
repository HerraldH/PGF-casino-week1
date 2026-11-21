# Programma opening,
print("-----------------------------------------------------")
print("Casino de Gouden Driehoek")
print("-----------------------------------------------------")

# Einde programma opening.
# -------------------------------------------- #

# Persoonsgegevens opvragen,
print("Vul uw Gegevens in")

# Voornaam opvragen
voornaam = input("Voornaam: ")

# Tussenvoegsel opvragen
tussenvoegsel = input("Tussenvoegsel: ")

# Achternaam opvragen
achternaam = input("Achternaam: ")

# Einde persoonsgegevens opvragen.
# -------------------------------------------- #

# Persoonsgegevens formatteren,

# [capitalized]
voornaam = voornaam.capitalize()
achternaam = achternaam.capitalize()

# [lowercase]
tussenvoegsel = tussenvoegsel.lower()

# Volledige naam
if tussenvoegsel != "":
    volledige_naam = f"{voornaam} {tussenvoegsel} {achternaam}"
elif tussenvoegsel == "":
    volledige_naam = f"{voornaam} {achternaam}"

# Einde persoonsgegevens formatteren.
# -------------------------------------------- #

# Geboortedatum,
# Format -> [dd-mm-yyyy]

print("-----------------------------------------------------")
print(f"Hallo {volledige_naam}.")
print("Wat is uw geboortedatum?")

# Geboortedatum opvragen
geboortedatum = input("[dd-mm-yyyy]: ")

# Geboortedatum format check,

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

# als niet oud genoeg → hier melding doen + programma afsluiten

# geen idee hoe ik kan rekenen met de actueele tijd / datum

print("-----------------------------------------------------")

# -------------------------------------------- #
# Geslacht [man, vrouw] --> [meneer, mevrouw]
print("Wat is uw geslacht?")
geslacht = input("[man, vrouw]: ")
print("-----------------------------------------------------")

# Welkom meneeer {naam}, wat is uw budget voor vandaag?
if geslacht == "man" or geslacht == "Man":
    aansprekingswoord = "meneer"
elif geslacht == "vrouw" or geslacht == "Vrouw":
    aansprekingswoord = "mevrouw"
else:
    aansprekingswoord = f" {str(voornaam[:1])}."

print(f"Welkom {aansprekingswoord} {achternaam}")
print("Wat is uw budget voor vandaag?")
budget = input("Budget: €")
# Maakt duidelijk dat het gaat om euro's en sla op als een float

# Vaste kosten aangeven, vraag gebruiker of hij budget wil aanpassen of niet?

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
print(f"Welkom, {aansprekingswoord} {achternaam}")
print("Bij Casino DGD hanteren wij de volgende vaste kosten.")
print("-----------------------------------------------------")
print(f"Toegangsticket:                               € {tt}")
print(f"Één verplicht drankje:                        € {vd}")
print(f"Gokbelasting:                                 € {gb}")
print(" ")
print(f"Totaal:                                       € {t} ")
print("-----------------------------------------------------")
print(" ")

# Vraag gebruiker om bevestiging / doorgaan

print("Gaat u hier mee akkoord?")
akkoord_vaste_kosten = input("Typ ['Y' voor akkoord] & ['N' voor niet akkoord]: ")

if akkoord_vaste_kosten == "Y" or akkoord_vaste_kosten == "y":
    print(" ")
else:
    print("Niet akkoord")
# geen idee hoe ik dit mooi kan laten doorlopen. heb nog niet goed kunnen uitzoeken hoe ik loops kan maken etc...


# "Uw buget voor vandaag is {bedrag} te weinig"
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
    print(f"Welkom, {aansprekingswoord} {achternaam}")
    print(f"Uw budget voor vandaag is €{float(budget) - float(t)}")
    print("-----------------------------------------------------")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("-----------------------------------------------------")
    print(" ")

# Final Output


# Volgorde van de maanden na checken
# Ga saldo afronden
# Vaste constanten boven aan de code zetten -> zoals TICKET_PRICE + Alles engelstalig maken
# Budget direct bij input omzetten naar een float
# dag, maand & jaar veranderen naar int i.p.v. float
# bij de gender controle kun je de controle net iets korter maken door `if geslacht.lower() == "man"` te doen.
# Dan zet hij zelf het geslacht al om naar kleine letters, en hoef je maar één controle uit te voeren.

# Maak betere comments, vertel niet wat iets doet, maar waarom het het doet
# code opschonen + verbeteren
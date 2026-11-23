


# Program opening,
print("-----------------------------------------------------")
print("Casino the Golden Triangle")
print("-----------------------------------------------------")
print("Please enter your information")
name = input("Name: ")
suffix = input("Suffix: ")
lastname = input("Lastname: ")

name = name.capitalize()
suffix = suffix.lower()
lastname = lastname.capitalize()

# The following code properly formats the full name,
if suffix != "":
    fullname = f"{name} {suffix} {lastname}"
elif suffix == "":
    fullname = f"{name} {lastname}"

# Requesting the users date of birth,
print("-----------------------------------------------------")
print(f"Hello {fullname}.")
print("Please enter your date of birth.")
birthday = input("[dd-mm-yyyy]: ")
if len(birthday) != 10:
    print("Error")

# The following code properly formats the date of birth and requests a confirmation from the user,
day = float(birthday[:2])
month = float(birthday[3:5])
year = float(birthday[6:])

if day <1 or day >31:
    print("Error")

if month <1 or month >12:
    print("Error")

if month == 1:
    month = "January"
elif month == 2:
    month = "February"
elif month == 3:
    month = "March"
elif month == 4:
    month = "April"
elif month == 5:
    month = "May"
elif month == 6:
    month = "June"
elif month == 7:
    month = "July"
elif month == 8:
    month = "August"
elif month == 9:
    month = "September"
elif month == 10:
    month = "October"
elif month == 11:
    month = "November"
elif month == 12:
    month = "December"

birthday_validation = f"{int(day)} {str(month)} {int(year)}"
print(f"Is your date of birth: {birthday_validation}?")
input("[Type ['Y' for yes] & ['N' for no]: ")

# TODO utilize the current date and time to validate if the user is old enough to enter the casino, shut down program if user is underage.

# Requesting and formatting the users gender.
print("-----------------------------------------------------")
print("Please enter your gender.")
gender = input("[male, female]: ")

if gender.lower == "male" or gender == "m":
    prefix = "Mr."
elif gender.lower() == "female" or gender == "f":
    prefix = "Ms."
else:
    prefix = f" {str(name[:1])}."

# Requesting the users budget for the day.
print("-----------------------------------------------------")
print(f"Welcome {prefix} {lastname}")
print("Please enter your budget for today.")
budget = input("Budget: €")

# TODO Make it clear that the requested budget is in euro's, then save data as a float.

# Vaste kosten aangeven, vraag gebruiker of hij budget wil aanpassen of niet?
# Values for the mandatory fees,
tt = "14.99"
vd = " 3.99"
gb = " 0.99"
t = float(tt) + float(vd) + float(gb)

# Requesting the user if he/she wants to change their budget, then requesting confirmation
print(" ")
print(" ")
print(" ")
print("-----------------------------------------------------")
print("Casino the Golden Triangle")
print("-----------------------------------------------------")
print(f"Welcome, {prefix} {lastname}")
print("At Casino TGT, we charge the following fixed fees.")
print("-----------------------------------------------------")
print(f"Entree fee:                                   € {tt}")
print(f"Mandatory drink:                              € {vd}")
print(f"Gambling tax:                                 € {gb}")
print(" ")
print(f"Total:                                        € {t} ")
print("-----------------------------------------------------")
print(" ")
print("Continue?")
akkoord_vaste_kosten = input("Type ['Y' for yes] & ['N' for no]: ")

# TODO Turn the above into a loop to properly validate the users input.

# Validating the users input,
if akkoord_vaste_kosten.lower() == "yes" or akkoord_vaste_kosten.lower() == "y":
    print(" ")
else:
    print("Error")

# TODO Tell the user by how much their budget for the day is insufficient.

if float(budget) < float(t):
    print("You're budget for today is insufficient.")
    print("Have a nice day.")
else:
    print(" ")
    print(" ")
    print(" ")
    print("-----------------------------------------------------")
    print("Casino the Golden Triangle")
    print("-----------------------------------------------------")
    print(f"Welcome, {prefix} {lastname}")
    print(f"Your budget for today is €{float(budget) - float(t)}")
    print("-----------------------------------------------------")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("-----------------------------------------------------")
    print(" ")

# TODO Round up the budget to a full integer.
# TODO Put fixed variables at the top of the code, Example: TICKET_PRICE.
# TODO Convert budget to a float directly when asking for input.
# TODO Change Day, Month, Year to integers instead of a float.
# TODO Gender validation should be shortend by doing the following: if gender.lower() == "male"

# TODO Improve the code and format it better.
# TODO Improve writing comments. Explain why the code does something, not what it does.


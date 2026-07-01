from core_logic.tracker import log_trip

while True:
    instructeur_naam = input("Geef hier de naam van de instructeur in, (of type 'stop' om te stoppen): ").lower()

    if instructeur_naam == "stop":
        print("Bye!")
        break

    kilometers = input("Geef hier het aantal gereden kilometers in: ")

    resultaat = log_trip(instructeur_naam, kilometers)
    print(resultaat)
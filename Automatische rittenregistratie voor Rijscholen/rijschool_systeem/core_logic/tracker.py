# Data-loop


def log_trip(instructeur_naam, kilometers):

    try:
        getransformeerde_kilometers = float(kilometers)

        with open("ritten_log.txt", "a") as file:
            file.write(f"Instructeur: {instructeur_naam} | Gereden: {getransformeerde_kilometers} km\n")
            return "Rit succesvol opgeslagen op de schijf!"
    
    except ValueError:
        return "Fout: Kilometers moeten in cijfers worden ingevoerd!"
    except IOError:
        return "Systeemfout: Harde schijf is niet bereikbaar! Rit kan niet worden opgeslagen."

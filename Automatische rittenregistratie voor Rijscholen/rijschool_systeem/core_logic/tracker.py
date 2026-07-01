# Data-loop


def log_ride(instructure_name, kilometers):

    try:
        transformed_kilometers = float(kilometers)

        with open("ritten_log.txt", "a") as file:
            file.write(f"Instructure: {instructure_name} | Driven: {transformed_kilometers} km\n")
            return "Ride successfully saved to disk!"
    
    except ValueError:
        return "Error: Kilometers must be entered in figures!"
    except IOError:
        return "System error: Hard drive is unreachable! Ride cannot be saved."

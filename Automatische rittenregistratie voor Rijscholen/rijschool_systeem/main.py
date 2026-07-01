from core_logic.tracker import log_trip

while True:
    instructure_name = input("Enter the instructor's name here, (or type 'stop' to stop): ").lower()

    if instructure_name == "stop":
        print("Bye!")
        break

    kilometers = input("Enter the number of kilometers driven here: ")

    result = log_ride(instructure_name, kilometers)
    print(result)

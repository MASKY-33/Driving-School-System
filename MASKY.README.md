# Driving School Trip‑Logger System
This system records driving‑lesson trips by saving the instructor’s name and the number of kilometers driven into a log file.
It uses a module, a package structure, and exception handling to safely write data to disk.

## Features
- Package structure:
- main.py → interaction with the instructor
- core_logic/ → package containing the logic
- tracker.py → module handling file writing
- Function log_trip() converts kilometers to a float
- Appends trip data to ritten_log.txt
- Handles invalid input (ValueError)
- Handles disk errors (IOError)
- Runs until the user types "stop"

# How to use
Enter the instructor’s name and the number of kilometers.
Valid input → trip saved to the log file.
Invalid or unreachable disk → clear error message.
Type "stop" to exit.


## Learning Purpose
Practice with:
- packages and modules
- file handling
- exception handling
- clean separation between logic and user interaction

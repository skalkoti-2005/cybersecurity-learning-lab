filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    print("Total log entries:", len(lines))

    errors = 0
    warnings = 0

    for line in lines:
        if "ERROR" in line.upper():
            errors += 1
        elif "WARNING" in line.upper():
            warnings += 1

    print("Errors:", errors)
    print("Warnings:", warnings)

except FileNotFoundError:
    print("Log file not found!")

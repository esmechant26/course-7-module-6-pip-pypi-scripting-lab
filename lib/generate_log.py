from datetime import datetime


def generate_log(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # Create filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write data to file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Return filename so tests can find it
    return filename
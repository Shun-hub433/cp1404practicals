"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)
    print(data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_records = []
    input_file = open(filename, "r")
    for line in input_file:
        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])
        subject_records.append(parts)

        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        #line = line.strip()  # Remove the \n
        #parts = line.split(',')  # Separate the data into its parts
        #print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        #data = [parts[0], parts[1], int(parts[2])]
        #print(data)  # See if that worked
        #print("----------")
    input_file.close()
    return subject_records


main()

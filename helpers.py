def get_input(day):
    """Takes in the day, returns the corresponding input as a string"""

    filename = "day-%s.input" % day
    with open(filename) as input_file:
        return [line.rstrip() for line in input_file.readlines()]

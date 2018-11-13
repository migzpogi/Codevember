def convert_miller_to_earth(hours_in_miller):
    """
    Converts number of hours spent in Miller's planet to Earth time
    :param hours_in_miller: Number of hours in Miller's Planet
    :return: Number of hours in Earth time
    """

    # basic formula is 1 hour in Miller's planet is 7 years in Earth
    # 7 years = 61,362 hours, 1 year = 8,766

    earth_hours = hours_in_miller * 61362
    return earth_hours

if __name__ == '__main__':
    miller_time = input("Please enter hours in Miller's Planet: ")
    earth_hours = convert_miller_to_earth(float(miller_time))

    print("That is {} hours in Earth time.".format(earth_hours))
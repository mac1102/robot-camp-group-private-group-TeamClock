def solution_station_5(name):

    total = 0
    for Uniformst in name.lower():
        if Uniformst in "uniformst":
            total += 1

    return total

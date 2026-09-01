def solution_station_5(name):
    vowels="eiou"
    total=0

    for letter in name.lower():
        if letter .isalpha() and letter not in vowels:
            total+=1
            
    return total

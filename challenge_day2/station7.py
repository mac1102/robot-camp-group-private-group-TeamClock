def solution_station_7(expression):
    variables = {
        "a": 3,
        "b": -1,
        "c": 4,
        "d": 7,
        "e": 0.5
    }
    result = eval(expression, {"__builtins__": {}}, variables)
    return float(result)


print((solution_station_7("b*c + d")))  
print((solution_station_7("d * e")))    
print((solution_station_7("d / c")))    
def solution_station_7(expression):
    variables = {
        "a": 3,
        "b": -1,
        "c": 4,
        "d": 7,
        "e": 0.5
    }
    expression = expression.replace("^", "**")
    result = eval(expression, {"__builtins__": {}}, variables)

    return float(result)
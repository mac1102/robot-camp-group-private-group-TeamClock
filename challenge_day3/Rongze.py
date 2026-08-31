def get_name():
    return "Rongze"


def get_character():
    return "Hans"

def act1(characters):
    return f"At the edge of the night market, {characters[3]} spotted {characters[0]} hagling over a strange lantern while {characters[1]} and {characters[2]} tried to slip away with the ___."

def act2(characters):
    return (
        f"{characters[0]} noticed the lantern was glowing brighter, while "
        f"{characters[3]} chased after {characters[1]} and {characters[2]}, who was runing toward the river."
    )

def act3(characters):
    return (
        f"In the end, {characters[0]}, {characters[1]}, {characters[2]}, and {characters[3]} "
        f"gathered around the lantern and discovered its light was actually a hidden secret."
    )
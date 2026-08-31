def get_name():
    return "an"

def get_team_intro():
    return "This is Team Clock. We are:"

def get_character_intro():
    return "These are the characters:"

def get_character():
    return 'Ben Dover'

def act1(characters):
    return f"{characters[0]} and {characters[1]} walkd into the forest while {characters[2]} and {characters[3]} waited near the ???."

def act2(characters):
    return (
        f"{characters[2]} notice a strange light behind the trees, while "
        f"{characters[0]}, {characters[1]}, and {characters[3]} tried to find the ???."
    )


def act3(characters):
    return (
        f"In the end, {characters[0]}, {characters[1]}, {characters[2]}, and "
        f"{characters[3]} discoverd that the mysterious light was actually ???."
    )
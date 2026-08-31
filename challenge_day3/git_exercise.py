import an
import Rakin
import yutong
import Rongze


def introduce_team():
    print(an.get_name())
    print(Rakin.get_name())
    print(yutong.get_name())
    print(Rongze.get_name())


def introduce_characters():
    print(an.get_character_intro())
    print(an.get_character())
    print(Rakin.get_character())
    print(yutong.get_character())
    print(Rongze.get_character())


def print_story():
    characters = [
        an.get_character(),
        Rakin.get_character(),
        yutong.get_character(),
        Rongze.get_character()
    ]

    print(an.act1(characters))
    print(an.act2(characters))
    print(an.act3(characters))


introduce_team()
introduce_characters()
print_story()
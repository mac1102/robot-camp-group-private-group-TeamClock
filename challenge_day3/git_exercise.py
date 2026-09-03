import an
import Rakin
import yutong
import Rongze
import yujie


def introduce_team():
    print(an.get_team_intro())
    print(an.get_name())
    print(Rakin.get_name())
    print(yutong.get_name())
    print(Rongze.get_name())
    print(yujie.get_name())


def introduce_characters():
    print(an.get_character_intro())
    print(an.get_character())
    print(Rakin.get_character())
    print(yutong.get_character())
    print(Rongze.get_character())
    print(yujie.get_character())


def print_story():
    characters = [
    an.get_character(),
    Rakin.get_character(),
    yutong.get_character(),
    Rongze.get_character(),
    yujie.get_character()
    ]

    # Act 1
    print(an.act1(characters))
    print(Rakin.act1(characters))
    print(yutong.act1(characters))
    print(Rongze.act1(characters))
    print(yujie.act1(characters))

    # Act 2
    print(an.act2(characters))
    print(Rakin.act2(characters))
    print(yutong.act2(characters))
    print(Rongze.act2(characters))
    print(yujie.act2(characters))

    # Act 3
    print(an.act3(characters))
    print(Rakin.act3(characters))
    print(yutong.act3(characters))
    print(Rongze.act3(characters))
    print(yujie.act3(characters))

introduce_team()
introduce_characters()
print_story()
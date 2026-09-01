from pandas import pd


def solution_station_5(name):
    df = pd.read_csv('learningteams.csv')

    number = df.loc[df['voornaam'] == name, 'lt']
    return number.values[0]





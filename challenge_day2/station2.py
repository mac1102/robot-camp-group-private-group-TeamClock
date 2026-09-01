from datetime import datetime

def solution_station_2(date):
    weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

    return weekdays[datetime.strptime(date, "%Y-%m-%d").weekday()]      
print(solution_station_2("2023-06-01"))
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class HabitObj:
    name: str
    data: dict[str, int]  # key = date, value = intensity


def process_habits_data(data: list[tuple[str, str, int]], days: int) -> list[HabitObj]:
    init_dates: dict[str, int] = {
        (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d"): 0
        for i in range(days)
    }
    temp: dict[str, dict[str, int]] = {}
    for date_str, tag_name, intensity in data:
        if tag_name not in temp:
            temp[tag_name] = init_dates.copy()
        if date_str in temp[tag_name]:
            temp[tag_name][date_str] = intensity

    result: list[HabitObj] = [
        HabitObj(name=tag, data=dates_dict) for tag, dates_dict in temp.items()
    ]
    return result

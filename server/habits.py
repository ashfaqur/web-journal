from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class HabitDataResult:
    habits: list[str]
    items: list[tuple[str, str, int]]


@dataclass
class HabitObj:
    name: str
    data: dict[str, int]  # key = date, value = intensity


def process_habits_data(data: HabitDataResult, days: int) -> list[HabitObj]:
    init_dates: dict[str, int] = {
        (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d"): 0
        for i in range(days)
    }
    temp: dict[str, dict[str, int]] = {}
    for date_str, tag_name, intensity in data.items:
        if tag_name not in temp:
            temp[tag_name] = init_dates.copy()
        if date_str in temp[tag_name]:
            temp[tag_name][date_str] = intensity

        # Add missing habits (ensure all habits are included)
    for habit in data.habits:
        if habit not in temp:
            temp[habit] = init_dates.copy()

    # Order the habits in the same order as the original habits list
    temp = {habit: temp[habit] for habit in data.habits}

    result: list[HabitObj] = [
        HabitObj(name=tag, data=dates_dict) for tag, dates_dict in temp.items()
    ]
    return result

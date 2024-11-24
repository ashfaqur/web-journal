from datetime import datetime


class Day:

    def __init__(self, date: datetime):
        self.date: datetime = date
        self.notes: list[str] = []

    def add_note(self, note: str) -> None:
        self.notes.append(note)

    def get_notes(self) -> list[str]:
        return self.notes

    def get_day_number(self) -> str:
        return self.date.strftime("%d")

    def __str__(self):
        return self.date.strftime("%d %B %Y")

    def print_notes(self) -> None:
        [print(note) for note in self.notes]


class Month:

    def __init__(self, date: datetime, days: list[Day]):
        self.date = date
        self.days = days

    def get_days(self):
        return self.days

    def __str__(self):
        return self.date.strftime("%B %Y")

    def print_month(self) -> None:
        print(self.date.strftime("%B %Y"))
        for day in self.days:
            day.print_notes()

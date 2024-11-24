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
        for note in self.notes:
            print(note)


class Month:

    def __init__(self, month_date: datetime, days: list[Day]):
        self.validate_parameters(month_date, days)
        self.date = month_date
        self.days = days

    def validate_parameters(self, month_date: datetime, days: list[Day]) -> None:
        # Ensure the month_date only specifies the year and month
        if month_date.day != 1 or month_date.time().second != 0:
            raise ValueError(
                "Month_date should only specify year and month, with default day and time."
            )

        # Validate all days fall within the given month and year
        for day in days:
            if day.date.year != month_date.year or day.date.month != month_date.month:
                raise ValueError(
                    f"Day {day.date.strftime('%d %B %Y')} does not fall within the month {month_date.strftime('%B %Y')}"
                )

    def get_days(self):
        return self.days

    def __str__(self):
        return self.date.strftime("%B %Y")

    def print_month(self) -> None:
        print(self.date.strftime("%B %Y"))
        for day in self.days:
            print(day.date.strftime("%d %B %Y"))
            day.print_notes()

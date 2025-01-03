import logging
import re
from pathlib import Path
from datetime import datetime
from journal_parser_model import Day
from journal_parser_model import Month
from sql import insert_journal_entrys

PATH_JOURNAL = "/home/ash/sb/daily-journal"

# Regex pattern for journal files matching YYYY Month.md
JOURANL_FILE_PATTERN = re.compile(
    r"^\d{4} (January|February|March|April|May|June|July|August|September|October|November|December)\.md$"
)


def parse_journal(path: str) -> list[Month]:
    logging.debug(f"Provided path to journal directory: '{path}'")

    # Convert the string path to a Path object
    journal_path = Path(path)

    # Check if the path exists and is a directory
    if not journal_path.is_dir():
        raise ValueError(
            f"The path '{path}' is not a valid directory or does not exist."
        )

    # Get a list of all files in the directory
    journal_files: list[Path] = [
        file
        for file in journal_path.iterdir()
        if file.is_file() and JOURANL_FILE_PATTERN.match(file.name)
    ]

    # Throw exception if there are no files
    if not journal_files:
        raise ValueError(f"No journal files found in '{path}'")

    # Print the list of files
    logging.debug(f"Files in '{path}': {journal_files}")

    months: list[Month] = []

    for journal_file in journal_files:
        month: Month = parseJournalfile(journal_file)
        # month.print_month()
        months.append(month)

    entries: list[tuple[str, int]] = []
    existing_dates: list[str] = []

    for month in months:
        for day in month.days:
            day.analyze_notes()
            date: str = day.date.strftime("%Y-%m-%d")
            if date in existing_dates:
                print(f"Entry already exists for {date}")
                continue
            existing_dates.append(date)
            entries.append((date, day.state.value))

        month.print_month()

    insert_journal_entrys(entries)

    return months


def parseJournalfile(journal_file: Path) -> Month:
    journal_month = journal_file.stem
    logging.debug(f"Processing Journal: {journal_month}")
    try:
        file_date = datetime.strptime(journal_month, "%Y %B")
    except ValueError:
        raise ValueError(
            f"Invalid journal file name: {journal_file.name}. Expected format: YYYY Month.md"
        )
    days: list[Day] = []
    with open(journal_file) as f:
        day: Day
        for line in f:
            content = line.rstrip()
            if not content:
                continue
            if content[0] == "#":
                date = content.split("#")[1].strip()
                if date:
                    try:
                        dayDate = datetime.strptime(date, "%d %B %Y")
                        day = Day(dayDate)
                        days.append(day)
                    except Exception:
                        print(f"{date} is invalid")
                        date = ""
                        continue
            elif day:
                day.add_note(content)

    return Month(file_date, days)


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=logging.DEBUG,
        datefmt="%H:%M:%S",
    )
    try:
        parse_journal(PATH_JOURNAL)
    except Exception as e:
        logging.error(e)

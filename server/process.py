from datetime import datetime, timedelta


def process_progress_data(
    items: list[tuple[str, str, int, int]],
) -> dict[str, list[tuple[str, int, int]]]:
    progress_list: dict[str, list[tuple[str, int, int]]] = {}
    for item in items:
        name: str = item[0]
        date: str = item[1]
        total_progress: int = item[2]
        daily_progress: int = item[3]
        if name in progress_list:
            progress_list[name].append((date, total_progress, daily_progress))
        else:
            progress_list[name] = [(date, total_progress, daily_progress)]

    for name in progress_list:
        # Add missing dates with 0 progress
        entries = progress_list[name]
        if entries:
            first_date_str: str = entries[0][0]
            first_date: datetime = datetime.strptime(first_date_str, "%Y-%m-%d")

            today_date: datetime = datetime.now()
            current_date = first_date
            full_entries: list[tuple[str, int, int]] = []
            i = 0
            while current_date <= today_date:
                current_date_str = current_date.strftime("%Y-%m-%d")
                if (i < len(entries)) and (entries[i][0] == current_date_str):
                    full_entries.append(entries[i])
                    i += 1
                else:
                    full_entries.append((current_date_str, entries[i - 1][1], 0))
                current_date += timedelta(days=1)
            progress_list[name] = full_entries

    return progress_list


def process_counter_data(
    items: list[tuple[str, str, int]],
) -> dict[str, list[dict]]:
    counter_group: dict[str, list[dict]] = {}
    for item in items:
        date: str = item[0]
        name: str = item[1]
        count: int = item[2]
        entry: dict = {"date": date, "count": count}

        if name not in counter_group:
            counter_group[name] = []
        counter_group[name].append(entry)

    # Get the first and last date for each group
    for name, entries in counter_group.items():
        if entries:
            first_date_str: str = entries[0]["date"]
            first_date: datetime = datetime.strptime(first_date_str, "%Y-%m-%d")
            last_date_str: str = entries[-1]["date"]
            last_date: datetime = datetime.strptime(last_date_str, "%Y-%m-%d")
            print(f"{name}: {first_date} - {last_date}")
            # loop over all the dates between the first and last date, and check if the entries dictionary contains that date
            current_date = first_date
            while current_date <= last_date:
                current_date_str = current_date.strftime("%Y-%m-%d")
                if not any(entry["date"] == current_date_str for entry in entries):
                    # If the date is missing, add a placeholder entry
                    entries.append({"date": current_date_str, "count": 0})
                current_date += timedelta(days=1)

            # sort the entries according to date
            entries.sort(key=lambda x: x["date"])
    return counter_group

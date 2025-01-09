import os
import re

# Regex pattern for journal files matching YYYY Month.md
JOURNAL_FILE_PATTERN = re.compile(
    r"^\d{4} (January|February|March|April|May|June|July|August|September|October|November|December)\.md$"
)


def get_journal_files(dir: str) -> list[str]:
    if dir:
        # Check if the path exists and is a directory
        if os.path.exists(dir) and os.path.isdir(dir):
            # Get a list of files in the directory
            files = os.listdir(dir)
            # Filter files that match the required format
            matching_files = [
                os.path.join(dir, f)
                for f in files
                if os.path.isfile(os.path.join(dir, f))
                and JOURNAL_FILE_PATTERN.match(f)
            ]
            return matching_files
        else:
            print(f"Path {dir} does not exist or is not a directory.")
    else:
        print("No directory to journal files is specified.")
    return []


def validate_journal_db_path(path: str) -> bool:
    return os.path.exists(path) and path.endswith(".db")

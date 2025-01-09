import os
import re
import subprocess
import logging

# Regex pattern for journal files matching YYYY Month.md
JOURNAL_FILE_PATTERN = re.compile(
    r"^\d{4} (January|February|March|April|May|June|July|August|September|October|November|December)\.md$"
)


def validate_journal_dir_env(dir: str) -> bool:
    if not dir:
        logging.debug("No directory to journal files is specified.")
        return False
    if not os.path.exists(dir):
        logging.debug(f"The directory '{dir}' does not exist.")
        return False
    if not os.path.isdir(dir):
        logging.debug(f"The path '{dir}' is not a directory.")
        return False
    # Use subprocess to check if it's a git repository
    try:
        result = subprocess.run(
            ["git", "-C", dir, "rev-parse", "--is-inside-work-tree"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return result.stdout.strip() == "true"
    except subprocess.CalledProcessError:
        return False


def update_journal_dir(dir: str) -> None:
    try:
        # Stash changes
        logging.debug("Stashing changes in the repository...")
        subprocess.run(
            ["git", "-C", dir, "stash"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True,
        )
        logging.debug("Changes stashed successfully.")

        # Switch to the main branch
        logging.debug("Stashing changes in the repository...")
        subprocess.run(
            ["git", "-C", dir, "checkout", "main"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True,
        )
        logging.debug("Switched to the main branch.")

        # Pull the latest changes
        logging.debug("Pulling the latest changes from the repository...")
        subprocess.run(
            ["git", "-C", dir, "pull", "--rebase"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True,
        )
        logging.info("Repository updated successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Git command failed: {e.stderr}")


def get_journal_files(dir: str) -> list[str]:
    if os.path.exists(dir) and os.path.isdir(dir):
        files = os.listdir(dir)
        matching_files = [
            os.path.join(dir, f)
            for f in files
            if os.path.isfile(os.path.join(dir, f)) and JOURNAL_FILE_PATTERN.match(f)
        ]
        return matching_files
    else:
        print(f"Path {dir} does not exist or is not a directory.")
    return []


def validate_journal_db_path_env(path: str) -> bool:
    if path:
        return path.endswith(".db")
    else:
        return False

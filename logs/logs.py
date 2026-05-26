import sys
from pathlib import Path
from collections import Counter


def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)

    if len(parts) != 4:
        raise ValueError("Incorrect log line format")
    date, time, level, message = parts

    return {
        'date': date,
        'time': time,
        "level": level,
        "message": message
    }

def load_logs(file_path: str) -> list:
    logs = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    logs.append(parse_log_line(line))

    except FileNotFoundError:
        print("Error: file not found")

    except PermissionError:
        print("Error: no permission to read this file")

    except ValueError:
        print("Error: incorrect log file format")

    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    # Functional approach used: filter + lambda
    return list(filter(lambda log: log["level"] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    counts = Counter(log["level"] for log in logs)

    return {
        "INFO": counts["INFO"],
        "ERROR": counts["ERROR"],
        "DEBUG": counts["DEBUG"],
        "WARNING": counts["WARNING"],
    }

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def display_logs(logs: list):
    for log in logs:
        print(f"{log['date']} {log['time']} {log['level']} {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py path/to/logfile.log [level]")
        return

    file_path = Path(sys.argv[1])

    logs = load_logs(str(file_path))

    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)

        print(f"\nДеталі логів для рівня '{level.upper()}':")
        display_logs(filtered_logs)


if __name__ == "__main__":
    main()

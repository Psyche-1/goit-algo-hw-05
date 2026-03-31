import sys
from pathlib import Path

def parse_log_line(line: str) -> dict[str, str]:
    """Function gets value from string"""
    date, time, level, message = line.strip().split(maxsplit=3)

    return {'date': date, 'time': time, 'level': level, 'message': message}

def load_logs(file_path: Path) -> list[dict[str, str]]:
    """Function opens a file and read it line by line"""
    try:
        with open(file_path) as file:
            logs = file.readlines()
    except ValueError:
        print('Errors while reading the file')
        return []
    
    return [parse_log_line(line) for line in logs]


def filter_logs_by_level(logs: list[dict[str, str]], level: str) -> list[dict[str, str]]:
    """Function returns only those logs that match the specified level"""
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list[dict[str, str]]) -> dict[str, int]:
    """Function calculate those logs that match the specified level"""
    logs_by_level: dict[str, int] = dict()

    for level in ['INFO', 'DEBUG', 'ERROR', 'WARNING']:
        logs_by_level[level] = len(filter_logs_by_level(logs, level))
    
    return logs_by_level

def display_log_counts(counts: dict[str, int]):
    """Function prints level and count of this level"""
    print('Рівень логування | Кількість')
    print('-----------------|----------')

    for level in counts:
        print(f"{level:<17}| {counts[level]}")
    
    print()

def display_log_details(logs: list[dict[str, str]], level: str):
    """Function prints details of logs"""
    filtered_logs = filter_logs_by_level(logs, level.upper())

    if level not in ['INFO', 'DEBUG', 'ERROR', 'WARNING']:
        print('Enter the correct level')
        return

    print(f"Деталі логів для рівня '{level.upper()}':")

    for log in filtered_logs:
        print(f'{log['date']} {log['time']} - {log['message']}')

def main():
    """Function takes command line arguments and run other function"""
    arguments = sys.argv
    len_arguments = len(arguments)

    if len_arguments < 2 or len_arguments > 3:
        print('Enter path to file')
        sys.exit()

    file_path = Path(arguments[1])

    if not file_path.is_file():
        print('Enter path to file')
        return

    logs = load_logs(file_path)
    display_log_counts(count_logs_by_level(logs))
    
    if len_arguments == 3:
        display_log_details(logs, arguments[2])

if __name__ == '__main__':
    main()

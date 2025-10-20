"""
Скрипт візуалізує структуру директорії з кольоровим виділенням.
Отримує шлях до директорії як аргумент у командному рядку та виводить
імена всіх піддиректорій і файлів у вигляді дерева.
"""
import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_tree(folder: Path, level: int = 0) -> None:
    try:
        for item in folder.iterdir():
            indent = "  " * level
            if item.is_dir():
                print(indent + Fore.BLUE + f"{item.name}/" + Style.RESET_ALL)
                print_tree(item, level + 1)
            else:
                print(indent + Fore.GREEN + item.name + Style.RESET_ALL)
    except PermissionError:
        print("  " * level + Fore.RED + "[Немає доступу]" + Style.RESET_ALL)

# старт скрипта
init(autoreset=True)

if len(sys.argv) != 2:
    print("Використання: python task_3.py C:\Windows\Help")
    raise SystemExit(1)

root = Path(sys.argv[1])

if not root.exists():
    print(Fore.RED + f"Помилка: шлях '{root}' не існує." + Style.RESET_ALL)
    raise SystemExit(1)

if not root.is_dir():
    print(Fore.RED + f"Помилка: '{root}' — це не директорія." + Style.RESET_ALL)
    raise SystemExit(1)

print(Style.BRIGHT + str(root.resolve()) + Style.RESET_ALL)
print_tree(root)
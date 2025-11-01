from pathlib import Path
from subprocess import run, CalledProcessError
from random import randrange
from time import sleep
import sys
import os
import platform

# Получаем путь к директории, где находится этот скрипт
BASE_DIR = Path(__file__).resolve().parent
COUNTER_FILE = BASE_DIR / "every_day.py"

def print_commit(number):
    border = '*' * 30
    return [border, f"*{'Всего коммитов':^28}*", f"*{str(number):^28}*", border]

def safe_git(*args):
    """Запускает git-команду и сообщает об ошибках."""
    try:
        result = run(["git", *args], cwd=BASE_DIR, check=True,
                     capture_output=True, text=True)
        return result.stdout.strip()
    except CalledProcessError as e:
        print(f"❌ Ошибка при выполнении git {' '.join(args)}:\n{e.stderr}")
        sys.exit(1)

def clear_screen():
    """Очищает экран терминала для любой ОС"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def check():
    clear_screen()  # Универсальная очистка терминала

    # Проверка, внутри ли мы git-репозитория
    try:
        run(["git", "rev-parse", "--is-inside-work-tree"],
            cwd=BASE_DIR, check=True, capture_output=True)
    except CalledProcessError:
        print("❌ Текущая директория не является git-репозиторием.")
        sys.exit(1)

    # Если файла нет — создаем с 1
    if not COUNTER_FILE.exists():
        COUNTER_FILE.write_text("# 1")

    # Читаем текущее значение
    current = int(COUNTER_FILE.read_text().split()[1])
    print(*print_commit(current), sep='\n')

    commits_to_make = randrange(3, 16)
    print(f"🔁 Коммитов запланировано: {commits_to_make}")

    for _ in range(commits_to_make):
        current += 1
        COUNTER_FILE.write_text(f"# {current}")

        # Git команды
        safe_git("add", str(COUNTER_FILE.relative_to(BASE_DIR)))
        safe_git("commit", "-m", f"{current}")
        safe_git("push", "origin", "main")
        print(f"✅ Коммит №{current} сделан")

    print(*print_commit(current), sep='\n')

if __name__ == "__main__":
    print("📥 Синхронизация с origin/main...")
    safe_git("pull", "origin", "main")
    sleep(2)
    check()
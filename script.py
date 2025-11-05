from pathlib import Path
from subprocess import run, CalledProcessError
from random import randrange
from time import sleep
import sys
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Получаем путь к директории, где находится этот скрипт
BASE_DIR = Path(__file__).resolve().parent
COUNTER_FILE = BASE_DIR / "every_day.py"


def print_commit(number):
    border = '*' * 30
    return [border, f"*{'Всего коммитов':^28}*", f"*{str(number):^28}*", border]


def safe_git(*args):
    """Запускает git-команду и сообщает об ошибках."""
    try:
        result = run(
            ["git", *args],
            cwd=BASE_DIR,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8"  # Добавлена кодировка
        )
        return result.stdout.strip()
    except CalledProcessError as e:
        print(f"❌ Ошибка при выполнении git {' '.join(args)}:\n{e.stderr}")
        sys.stdout.flush()  # Add flush here
        sys.exit(1)


def clear_screen():
    """Очищает экран терминала."""
    os.system('cls' if os.name == 'nt' else 'clear')


def check():
    clear_screen()  # Очистка терминала

    # Проверка, внутри ли мы git-репозитория
    try:
        run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=BASE_DIR,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8"  # Добавлена кодировка
        )
    except CalledProcessError:
        print("❌ Текущая директория не является git-репозиторием.")
        sys.stdout.flush()  # Add flush here
        sys.exit(1)

    # Если файла нет — создаем с 1
    if not COUNTER_FILE.exists():
        COUNTER_FILE.write_text("# 1", encoding="utf-8")  # Добавлена кодировка

    # Читаем текущее значение
    try:
        with open(COUNTER_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            parts = content.split()
            if len(parts) > 1:
                current = int(parts[1])
            else:
                current = 0  # Или другое значение по умолчанию
    except FileNotFoundError:
        print(f"❌ Файл не найден: {COUNTER_FILE}")
        sys.stdout.flush()  # Add flush here
        sys.exit(1)
    except ValueError:
        print(
            f"❌ Ошибка: Не удалось преобразовать содержимое файла {COUNTER_FILE} в число.")
        sys.stdout.flush()  # Add flush here
        sys.exit(1)

    print(*print_commit(current), sep='\n')
    sys.stdout.flush()  # Add flush here

    commits_to_make = randrange(3, 16)
    print(f"🔁 Коммитов запланировано: {commits_to_make}")
    sys.stdout.flush()  # Add flush here

    for _ in range(commits_to_make):
        current += 1
        # Добавлена кодировка
        COUNTER_FILE.write_text(f"# {current}", encoding="utf-8")

        # Git команды
        safe_git("add", str(COUNTER_FILE.relative_to(BASE_DIR)))
        safe_git("commit", "-m", f"{current}")
        safe_git("push", "origin", "main")
        print(f"✅ Коммит №{current} сделан")
        sys.stdout.flush()  # Add flush here

    print(*print_commit(current), sep='\n')
    sys.stdout.flush()  # Add flush here


if __name__ == "__main__":
    print("📥 Синхронизация с origin/main...")
    sys.stdout.flush()  # Add flush here
    try:
        safe_git("pull", "origin", "main")
    except Exception as e:
        print(f"❌ Ошибка при выполнении git pull: {e}")
        sys.stdout.flush()  # Add flush here
        sys.exit(1)
    sleep(2)
    check()

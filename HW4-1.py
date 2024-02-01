from pathlib import Path
import sys


def total_salary(path):
    try:
        with open(
        "d:\\goit\\goit-algo-hw-04\\goit-algo-hw-04\\path.txt", "r", encoding="cp1251") as file:
            lines = file.readlines()
        total = 0
        num_dev = len(lines)

        for line in lines:
            _, salary_str = line.strip().split(',')
            salary = float(salary_str)
            total += salary

        average = total / num_dev

        return total, average

    except FileNotFoundError:
        print(f"Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None


file_path = "d:\\goit\\goit-algo-hw-04\\goit-algo-hw-04\\path.txt"
result = total_salary(file_path)

if result:
    total, average = result

    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

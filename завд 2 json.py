import json
import os
import unicodedata
import re
from typing import List, Dict, Any

# -------------------------------------------------------------
# ФАЙЛ ДАНИХ
# -------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "schools_db.json")
RESULT_FILE = os.path.join(SCRIPT_DIR, "result.json")

SchoolData = List[Dict[str, Any]]


# -------------------------------------------------------------
# DEFAULT DATA
# -------------------------------------------------------------
def get_default_data() -> SchoolData:
    return [
        {"name": "Сумський державний університет", "type": "університет", "students": 25000},
        {"name": "Школа №10", "type": "школа", "students": 1500},
        {"name": "Машинобудівний коледж", "type": "коледж", "students": 510},
        {"name": "Школа №29", "type": "школа", "students": 720},
        {"name": "Школа №25", "type": "школа", "students": 560},
        {"name": "Київський політехнічний інститут", "type": "інститут", "students": 52350}
    ]


# -------------------------------------------------------------
# FILE OPERATIONS
# -------------------------------------------------------------
def load_data(filename: str) -> SchoolData:
    if not os.path.exists(filename):
        data = get_default_data()
        save_data(filename, data)
        return data

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(filename: str, data: Any) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# -------------------------------------------------------------
# NORMALIZATION FOR SEARCH
# -------------------------------------------------------------
def normalize(text: str) -> str:
    text = text.strip().lower()
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("№", "#")
    text = re.sub(r"\s+", " ", text)
    return text


# -------------------------------------------------------------
# DISPLAY ALL
# -------------------------------------------------------------
def display_all(filename: str) -> None:
    data = load_data(filename)
    print("\n--- Список навчальних закладів ---")
    for item in data:
        print(f"{item['name']} — {item['type']}, учнів: {item['students']}")


# -------------------------------------------------------------
# ADD NEW RECORD
# -------------------------------------------------------------
def add_record(filename: str) -> None:
    data = load_data(filename)

    print("\n--- Додавання нового запису ---")
    name = input("Назва закладу: ")
    type_ = input("Тип (школа / коледж / технікум / інститут / університет): ")
    students = int(input("Кількість учнів: "))

    data.append({"name": name, "type": type_, "students": students})
    save_data(filename, data)

    print("Запис успішно додано!")


# -------------------------------------------------------------
# DELETE RECORD
# -------------------------------------------------------------
def delete_record(filename: str) -> None:
    data = load_data(filename)

    print("\n--- Видалення запису ---")
    name = input("Введіть назву закладу для видалення: ")

    new_data = [item for item in data if normalize(item["name"]) != normalize(name)]

    if len(new_data) == len(data):
        print("Запис не знайдено!")
    else:
        save_data(filename, new_data)
        print("Запис успішно видалено!")


# -------------------------------------------------------------
# SEARCH
# -------------------------------------------------------------
def search_data(filename: str) -> None:
    data = load_data(filename)

    print("\n--- Пошук даних ---")
    field = input("Поле (name/type/students): ").strip()
    value = input("Значення для пошуку: ")

    if field == "students":
        value = int(value)

    print("\nРезультати пошуку:")
    for item in data:
        if str(item.get(field)).lower() == str(value).lower():
            print(item)


# -------------------------------------------------------------
# TOTAL STUDENTS IN SCHOOLS (VARIANT TASK)
# -------------------------------------------------------------
def calc_total_school_students(filename: str) -> None:
    data = load_data(filename)
    total = sum(item["students"] for item in data if normalize(item["type"]) == "школа")

    result = {"total_school_students": total}
    save_data(RESULT_FILE, result)

    print("\n--- Загальна кількість учнів у школах ---")
    print(f"Всього учнів у школах: {total}")
    print(f"Результат записано у файл {RESULT_FILE}")


# -------------------------------------------------------------
# MENU
# -------------------------------------------------------------
def print_menu():
    print("\n--- Меню ---")
    print("1. Показати всі записи")
    print("2. Додати новий запис")
    print("3. Видалити запис")
    print("4. Пошук у файлі")
    print("5. Порахувати учнів у школах (записати в інший JSON)")
    print("6. Вийти")


# -------------------------------------------------------------
# MAIN
# -------------------------------------------------------------
def main():
    load_data(DATA_FILE)

    while True:
        print_menu()
        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            display_all(DATA_FILE)
        elif choice == "2":
            add_record(DATA_FILE)
        elif choice == "3":
            delete_record(DATA_FILE)
        elif choice == "4":
            search_data(DATA_FILE)
        elif choice == "5":
            calc_total_school_students(DATA_FILE)
        elif choice == "6":
            print("До побачення!")
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main()

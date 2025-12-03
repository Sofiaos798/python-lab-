import csv
import matplotlib.pyplot as plt
import os
import sys
from typing import Dict, List, Any, Tuple

DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILENAME = os.path.join(DIR, "lab10.csv")

def get_data_from_csv(filename: str) -> Dict[str, Any]:
    # зчитує дані з CSV файлу, повертає словник
    data = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # отримуємо назви колонок з роками
            year_columns = [col for col in reader.fieldnames if '[YR' in col]
            
            for row in reader:
                country_name = row.get('Country Name')
                if not country_name:
                    continue

                country_data = []
                for col in year_columns:
                    val_str = row.get(col, '..')
                    
                    # очистка року
                    year_str = col.split(' [')[0]
                    
                    # обробка значення ".."
                    if val_str and val_str != '..':
                        try:
                            year = int(year_str)
                            value = float(val_str)
                            country_data.append((year, value))
                        except ValueError:
                            continue
                
                if country_data:
                    # сортуємо за роком
                    country_data.sort(key=lambda x: x[0])
                    data[country_name] = country_data
                    
        print(f"Успішно завантажено дані для {len(data)} країн.")
        return data

    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        print("Будь ласка, перейменуйте завантажений файл у 'lab10.csv' і покладіть поруч зі скриптом.")
        return {}
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return {}

def plot_comparison(data: Dict[str, Any], country1: str, country2: str) -> None:
    # 2.1. графік динаміки показника для двох країн на одній координатній осі
    print(f"\n--- Побудова графіку порівняння: {country1} vs {country2} ---")
    
    if country1 not in data or country2 not in data:
        print("Помилка: Однієї з країн немає в базі даних.")
        return

    # підготовка даних для 1 країни
    c1_data = data[country1]
    x1 = [item[0] for item in c1_data]
    y1 = [item[1] for item in c1_data]

    # підготовка даних для 2 країни
    c2_data = data[country2]
    x2 = [item[0] for item in c2_data]
    y2 = [item[1] for item in c2_data]

    plt.figure(figsize=(10, 6))
    
    # побудова ліній
    plt.plot(x1, y1, label=country1, color='blue', linewidth=2, marker='o', markersize=4)
    plt.plot(x2, y2, label=country2, color='red', linewidth=2, marker='s', markersize=4)

    # оформлення
    plt.title(f"Динаміка GDP per capita: {country1} та {country2}", fontsize=14)
    plt.xlabel("Рік", fontsize=12, color='darkblue')
    plt.ylabel("ВВП на душу населення (поточні US$)", fontsize=12, color='darkblue')
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # форматування осі x, щоб показувати всі роки
    all_years = sorted(list(set(x1 + x2)))
    plt.xticks(all_years[::2], rotation=45)
    
    plt.tight_layout()
    print("Графік побудовано.")
    plt.show()

def plot_bar_chart(data: Dict[str, Any]) -> None:
    # 2.2. стовпчаста діаграма для вибраної країни
    print("\n--- Побудова стовпчастої діаграми ---")
    country_name = input("Введіть назву країни (наприклад, Ukraine, Poland, United States): ").strip()
    
    # спроба знайти країну
    found_key = None
    for key in data.keys():
        if key.lower() == country_name.lower():
            found_key = key
            break
    
    if found_key:
        c_data = data[found_key]
        years = [item[0] for item in c_data]
        values = [item[1] for item in c_data]
        
        plt.figure(figsize=(10, 6))
        
        # стовпчаста діаграма
        bars = plt.bar(years, values, color='green', alpha=0.7, edgecolor='black')
        
        plt.title(f"ВВП на душу населення: {found_key}", fontsize=14)
        plt.xlabel("Рік", fontsize=12)
        plt.ylabel("US$", fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xticks(years, rotation=45)
        
        plt.tight_layout()
        print(f"Діаграму для '{found_key}' побудовано.")
        plt.show()
    else:
        print(f"Помилка: Країну '{country_name}' не знайдено.")

def print_menu() -> None:
    print("\n--- Меню ---")
    print("1. Порівняти динаміку ВВП двох країн")
    print("2. Побудувати стовпчасту діаграму для країни")
    print("3. Вийти")

def main() -> None:
    # завантажуємо дані
    print("Завантаження даних...")
    db = get_data_from_csv(CSV_FILENAME)
    
    if not db:
        print("Роботу програми зупинено через відсутність даних.")
        return

    while True:
        print_menu()
        choice = input("Ваш вибір (1-3): ").strip()
        
        if choice == '1':
            # 2.1 порівняння двох країн
            print("\n--- Ввід країн для порівняння ---")
            c1 = input("Введіть назву першої країни (наприклад, Ukraine): ").strip()
            c2 = input("Введіть назву другої країни (наприклад, Poland): ").strip()
            
            # перевірка
            if c1 and c2:
                plot_comparison(db, c1, c2)
            else:
                print("Помилка: Назви країн не можуть бути порожніми.")
        
        elif choice == '2':
            # 2.2 стовпчаста діаграма
            plot_bar_chart(db)
            
        elif choice == '3':
            print("Завершення роботи. До побачення!")
            break
            
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
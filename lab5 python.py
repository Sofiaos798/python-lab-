# Початкові дані про n=6 навчальних закладів:
INSTITUTIONS_DB = {
    "Школа №10": (1500, "школа"),
    "Сумський державний університет": (25000, "університет"),
    "Машинобудівний коледж": (510, "коледж"),
    "Кихвський політехнічний інститут": (52350, "інститут"),
    "Школа №25": (620, "школа"),
    "Школа №29": (750, "школа")
}

def display_all_institutions(db: dict) -> None:
    """Виводить на екран всі значення (назви, учні, тип) зі словника."""
    print("\n--- Повний список навчальних закладів ---")
    if not db:
        print("База даних закладів порожня.")
        return
    
    
    for name, data in db.items():
        students, school_type = data
        print(f"Заклад: {name}, Учні: {students}, Тип: {school_type.capitalize()}")



def add_institution(db: dict) -> None:
    """Додає новий запис (заклад) до словника."""
    print("\n--- Додавання нового закладу ---")
    
    
    while True:
        name = input("Введіть назву нового закладу: ").strip()
        if not name:
            print("Помилка: Назва закладу не може бути порожньою.")
        elif name in db:
            print(f"Помилка: Заклад з назвою '{name}' вже є у базі.")
        else:
            break
            
    #  Введення кількості учнів
    while True:
        students_str = input(f"Введіть кількість учнів для '{name}': ").strip()
        if not students_str.isdigit():
            print("Помилка: Кількість учнів має бути додатним цілим числом.")
        else:
            students = int(students_str)
            if students <= 0:
                 print("Помилка: Кількість учнів має бути більшою за 0.")
            else:
                break
                
    # Введення типу закладу
    valid_types = {'школа', 'інститут', 'університет'}
    while True:
        school_type = input(f"Введіть тип закладу ('школа', 'інститут' або 'університет') для '{name}': ").strip().lower()
        if school_type not in valid_types:
            print(f"Помилка: Невірний тип закладу. Дозволено: {', '.join(valid_types)}")
        else:
            break
            
    #  Додавання до словника
    db[name] = (students, school_type)
    print(f"Заклад '{name}' ({school_type.capitalize()}) з {students} учнями успішно додано.")

def delete_institution(db: dict) -> None:
    """Видаляє запис (заклад) зі словника за ключем (назвою)."""
    print("\n--- Видалення закладу ---")
    name_to_delete = input("Введіть точну назву закладу, який хочете видалити: ").strip()
    
    if not name_to_delete:
        print("Помилка: Назва закладу не може бути порожньою.")
        return

    if name_to_delete in db:
        students, school_type = db[name_to_delete]
        print(f"Ви впевнені, що хочете видалити: {name_to_delete} (Тип: {school_type.capitalize()}, Учні: {students})?")
        confirmation = input("Введіть 'так' для підтвердження: ").strip().lower()
        
        if confirmation == 'так':
            del db[name_to_delete]
            print(f"Заклад '{name_to_delete}' успішно видалено.")
        else:
            print("Видалення скасовано.")
    else:
        print(f"Помилка: Закладу з назвою '{name_to_delete}' не знайдено в базі.")

def display_sorted_institutions(db: dict) -> None:
    """Виводить вміст словника, відсортований за ключами (назвами закладів)."""
    print("\n--- Список закладів (відсортовано за назвою) ---")
    if not db:
        print("База даних закладів порожня.")
        return
        
    try:
        
        sorted_keys = sorted(db.keys())
        for name in sorted_keys:
            students, school_type = db[name]
            print(f"Заклад: {name}, Учні: {students}, Тип: {school_type.capitalize()}")
    except Exception as e:
        print(f"Сталася помилка під час сортування: {e}")


def calculate_school_students(db: dict) -> None:
    """Визначає загальну кількість учнів у всіх закладах типу 'школа'."""
    print("\n--- Загальна кількість учнів шкіл ---")
    
    if not db:
        print("Помилка: База даних закладів порожня. Неможливо провести розрахунок.")
        return

    total_school_students = 0
    school_list = []
    
    for name, data in db.items():
        students, school_type = data
        
        # Перевірка типу закладу
        if school_type == 'школа':
            total_school_students += students
            school_list.append(name)

    print(f"Знайдені школи: {', '.join(school_list)}")
    print(f" Загальна кількість учнів у школах: **{total_school_students}**")



def print_menu() -> None:
    """Виводить головне меню програми."""
    print("\n--- Меню Обліку Учнів ---")
    print("1. Вивести повний список закладів")
    print("2. Додати новий заклад до бази")
    print("3. Видалити заклад з бази")
    print("4. Вивести список (відсортовано за назвою)")
    print("5. Визначити загальну кількість учнів шкіл (Завдання)")
    print("6. Вийти з програми")

def main() -> None:
    """Головна функція програми. Керує діалогом з користувачем."""
    
    current_db = INSTITUTIONS_DB.copy()
    
    while True:
        print_menu()
        choice = input("Введіть ваш вибір (1-6): ").strip()
        
        if choice == '1':
            display_all_institutions(current_db)
        
        elif choice == '2':
            add_institution(current_db)
            
        elif choice == '3':
            delete_institution(current_db)
            
        elif choice == '4':
            display_sorted_institutions(current_db)
            
        elif choice == '5':
            calculate_school_students(current_db)
            
        elif choice == '6':
            print("Завершення роботи програми. До побачення!")
            break
            
        else:
            print("Помилка: Неправильний вибір. Введіть число від 1 до 6.")

if __name__ == "__main__":
    main()

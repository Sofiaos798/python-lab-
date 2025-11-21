import pandas as pd
import matplotlib.pyplot as plt
import os

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILENAME = os.path.join(DIR, "comptagevelo2014.csv")  

def load_and_clean_data(filename: str) -> pd.DataFrame:
    try:
        
        df = pd.read_csv(
            filename,
            sep=',',
            encoding='latin1'
        )

        
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        # видаляємо рядки, де дата не зчиталась
        df = df.dropna(subset=['Date'])

        # робимо дату індексом
        df = df.set_index('Date')

        df = df.select_dtypes(include=['number'])

        print(f"Файл '{filename}' успішно завантажено.")
        return df

    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return pd.DataFrame()

def display_basic_info(df: pd.DataFrame) -> None:
    print("\n--- Перші 5 рядків (head) ---")
    print(df.head())

    print("\n--- Інформація про типи даних (info) ---")
    print(df.info())

    print("\n--- Описова статистика (describe) ---")
    print(df.describe())

def analyze_total_usage(df: pd.DataFrame) -> None:
    print("\n--- Загальна статистика за рік ---")
    total_cyclists = df.sum().sum()
    print(f"Загальна кількість велосипедистів на всіх доріжках: {int(total_cyclists)}")

    print("\n--- Кількість велосипедистів по кожній велодоріжці ---")
    per_path_counts = df.sum()
    for path, count in per_path_counts.items():
        print(f"  {path}: {int(count)}")

def analyze_most_popular_month(df: pd.DataFrame) -> None:
    print("\n--- Найпопулярніші місяці ---")
    monthly_df = df.resample('ME').sum()

    selected_paths = df.columns[:3].tolist()
    for path in selected_paths:
        max_date = monthly_df[path].idxmax()
        max_value = monthly_df[path].max()
        month = max_date.strftime('%B')
        print(f"Для '{path}' найпопулярніший місяць: {month} ({int(max_value)} велосипедистів)")

def plot_path_usage(df: pd.DataFrame) -> None:
    print("\n--- Побудова графіку ---")
    paths = df.columns.tolist()
    print(f"Доступні велодоріжки: {', '.join(paths)}")

    path_name = input("Введіть назву велодоріжки (наприклад, Berri1): ").strip()

    if path_name in df.columns:
        monthly_data = df[path_name].resample('ME').sum()
        monthly_data.plot(marker='o')

        plt.title(f"Завантаженість велодоріжки {path_name} по місяцях (2014)")
        plt.xlabel("Місяць")
        plt.ylabel("Кількість велосипедистів")
        plt.grid(True)
        plt.show()
    else:
        print("Помилка: такої велодоріжки не існує.")

def print_menu() -> None:
    print("\n--- Головне Меню ---")
    print("1. Перевірити характеристики датафрейму")
    print("2. Визначити загальну кількість велосипедистів")
    print("3. Визначити найпопулярніший місяць")
    print("4. Побудувати графік завантаженості по місяцях")
    print("5. Вийти")

def main() -> None:
    df = load_and_clean_data(CSV_FILENAME)

    if df.empty:
        print("Роботу зупинено — дані відсутні.")
        return

    while True:
        print_menu()
        choice = input("Ваш вибір (1-5): ").strip()

        if choice == '1':
            display_basic_info(df)
        elif choice == '2':
            analyze_total_usage(df)
        elif choice == '3':
            analyze_most_popular_month(df)
        elif choice == '4':
            plot_path_usage(df)
        elif choice == '5':
            print("До побачення!")
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()

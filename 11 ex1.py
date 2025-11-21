import pandas as pd

# Дані з практичної роботи №5
INSTITUTIONS_DB = {
    "Школа №10": (1500, "школа"),
    "Сумський державний університет": (25000, "університет"),
    "Машинобудівний коледж": (510, "коледж"),
    "Кихвський політехнічний університет": (52350, "університет"),
    "Школа №25": (620, "школа"),
    "Школа №29": (750, "школа")
}

# Створення DataFrame
df = pd.DataFrame([
    {"Name": name, "Students": students, "Type": school_type}
    for name, (students, school_type) in INSTITUTIONS_DB.items()
])

# Виведення DataFrame
print("=== DataFrame ===")
print(df)

# Перші 3 рядки
print("\n=== df.head(3) ===")
print(df.head(3))

# Типи даних
print("\n=== df.dtypes ===")
print(df.dtypes)

# Кількість рядків і стовпців
print("\n=== df.shape ===")
print(df.shape)

# Описова статистика
print("\n=== df.describe() ===")
print(df.describe())

# Додаємо стовпець з розрахунковим значенням
# Наприклад: бюджет на 1 учня для кожного типу
budget_per_student = {
    "школа": 2000,
    "університет": 8000,
    "коледж": 3500
}

df["Budget_per_student"] = df["Type"].map(budget_per_student)
df["Total_budget"] = df["Students"] * df["Budget_per_student"]

print("\n=== DataFrame з новими стовпцями ===")
print(df)

# Фільтрація: заклади з бюджетом більше 50 млн
print("\n=== Фільтрація Total_budget > 50 000 000 ===")
print(df[df["Total_budget"] > 50_000_000])

# Сортування: за спаданням Students
print("\n=== Сортування за спаданням Students ===")
print(df.sort_values(by="Students", ascending=False))

# Групування: середня кількість студентів по типах
print("\n=== Групування: середні значення по типах ===")
print(df.groupby("Type").mean(numeric_only=True))

# Максимальна сума бюджету в категорії
print("\n=== Максимальний бюджет у кожному типі ===")
print(df.groupby("Type")["Total_budget"].max())

# Кількість унікальних типів закладів
print("\n=== Кількість унікальних типів ===")
print(df["Type"].nunique())

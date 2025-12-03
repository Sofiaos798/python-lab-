import json
import os
import matplotlib.pyplot as plt
import numpy as np

# шлях до файлу
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "schools_db.json")

def load_data(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def plot_pie_chart(filename: str) -> None:
    # завантаження JSON
    data = load_data(filename)

    # витягуємо назви та кількість студентів
    labels = [item["name"] for item in data]
    values = [item["students"] for item in data]

    # створення діаграми
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))

    def func(pct, allvals):
        absolute = int(np.round(pct / 100.0 * np.sum(allvals)))
        return f"{pct:.1f}%\n({absolute})"

    wedges, texts, autotexts = ax.pie(
        values,
        autopct=lambda pct: func(pct, values),
        textprops=dict(color="white")
    )

    # легенда
    ax.legend(
        wedges,
        labels,
        title="Навчальні заклади",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1)
    )

    plt.setp(autotexts, size=9, weight="bold")
    ax.set_title("Розподіл студентів між навчальними закладами")

    plt.show()


# тестовий запуск (можна видалити якщо додаватимете в меню)
if __name__ == "__main__":
    plot_pie_chart(DATA_FILE)

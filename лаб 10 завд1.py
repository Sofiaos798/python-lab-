import matplotlib.pyplot as plt
import numpy as np

def plot_function() -> None:
    # створення масиву x (починаємо з 0.001, щоб уникнути ділення на 0)
    x = np.linspace(0.001, 10, 500)

    # обчислення функції
    y = -5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

    # побудова графіку
    plt.plot(x, y, label='-5*cos(10*x)*sin(3*x)/sqrt(x)',
             color='green', linewidth=2.5, linestyle='-')

    # оформлення
    plt.title('Графік функції', fontsize=14)

    # позначення осей
    plt.xlabel('Значення x', fontsize=12, color='darkblue')
    plt.ylabel('Значення Y(x)', fontsize=12, color='darkblue')

    # легенда та сітка
    plt.legend()
    plt.grid(True)

    # вивід графіку
    print("Побудова графіку завершена. Відкриття вікна...")
    plt.show()

def main() -> None:
    try:
        plot_function()
    except Exception as e:
        print(f"Виникла неочікувана помилка при побудові графіку: {e}")

if __name__ == "__main__":
    main()

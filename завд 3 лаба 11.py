import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import string
import sys


def ensure_nltk_data() -> None:
    """Переконується, що всі потрібні корпуси NLTK доступні."""
    print("Перевірка наявності корпусів NLTK...")
    required_packages = ['gutenberg', 'stopwords', 'punkt']

    for pkg in required_packages:
        try:
            nltk.data.find(f"corpora/{pkg}")
        except LookupError:
            print(f"Пакет '{pkg}' не знайдений. Завантажую...")
            nltk.download(pkg, quiet=True)

    print("Усі необхідні ресурси готові до роботи.")


def load_text_tokens(file_id: str) -> list[str]:
    """Завантажує слова з корпусу Gutenberg."""
    try:
        print(f"\nЗавантаження '{file_id}'...")
        return list(gutenberg.words(file_id))
    except Exception as exc:
        print(f"Не вдалося прочитати файл: {exc}")
        sys.exit(1)


def visualize_frequencies(fdist: FreqDist, caption: str, n: int = 10) -> None:
    """Відображає графік із n найчастотніших слів."""
    print(f"\nГрафік: {caption}")

    common = fdist.most_common(n)
    words = [w for w, _ in common]
    counts = [c for _, c in common]

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.title(caption)
    plt.xlabel("Слово")
    plt.ylabel("Частотність")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

    print(f"Топ-{n}: {common}")


def preprocess_tokens(tokens: list[str]) -> list[str]:
    """Очищає слова: видаляє пунктуацію, стоп-слова та залишає лише алфавітні."""
    print("\nОчищення тексту...")

    eng_stopwords = set(stopwords.words("english"))
    punctuation_marks = set(string.punctuation)

    processed = [
        token.lower()
        for token in tokens
        if token.isalpha()
        and token.lower() not in eng_stopwords
        and token not in punctuation_marks
    ]

    print(f"Кількість слів після очищення: {len(processed)}")
    return processed


def main() -> None:
    ensure_nltk_data()

    text_id = "chesterton-brown.txt"  

    tokens = load_text_tokens(text_id)
    print(f"Усього слів у тексті: {len(tokens)}")

    
    raw_freq = FreqDist(tokens)
    visualize_frequencies(raw_freq, f"Топ-10 слів у '{text_id}'")


    cleaned_tokens = preprocess_tokens(tokens)

    # 10 найчастіших слів після очищення
    clean_freq = FreqDist(cleaned_tokens)
    visualize_frequencies(clean_freq, f"Топ-10 слів у '{text_id}' після очищення")


if __name__ == "__main__":
    main()

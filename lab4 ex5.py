def analyze_text():
    text = input("Введіть текст (малими латинськими літерами): ")

    letters = {ch for ch in text if ch.isalpha()}

    punctuation_marks = {'.', ',', '!', '?', ':', ';', '-', '(', ')', '"', "'"}
    count_punct = sum(1 for ch in text if ch in punctuation_marks)

    print("Множина літер у тексті:", letters)
    print("Кількість розділових знаків:", count_punct)

    return letters, count_punct

analyze_text()

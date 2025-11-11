# Функція для безпечного відкриття файлу
def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("Файл", file_name, "не вдалося відкрити!")
        return None
    else:
        print("Файл", file_name, "успішно відкрито!")
        return file


# Імена файлів
file1_name = "TF13_1.txt"
file2_name = "TF13_2.txt"

# === а) Створення текстового файлу TF13_1 ===
file_1_w = Open(file1_name, "w")
if file_1_w is not None:
    text = """І їй рука чоловіча
Віку вкоротила.
Ой понесли конвалію
У високу залу,
Понесла її з собою
Панночка до балу."""
    
    file_1_w.write(text)
    print("Інформацію успішно записано у TF13_1.txt!")
    file_1_w.close()
    print("Файл TF13_1.txt закрито!")


# === б) Читання TF13_1 і запис слів, що починаються з голосної ===
file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r is not None and file_2_w is not None:
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    import re

    # Зчитуємо увесь текст і розбиваємо на слова, ігноруючи розділові знаки
    words = re.findall(r"[А-Яа-яЇїІіЄєA-Za-z']+", file_2_r.read())

    for word in words:
        if word[0] in vowels:
            file_2_w.write(word + "\n")

    file_2_r.close()
    file_2_w.close()
    print("Слова, що починаються з голосної, записані у TF13_2.txt!")


# === в) Читання TF13_2 і друк по рядках ===
print("\nСлова з TF13_2.txt:")
file_3_r = Open(file2_name, "r")

if file_3_r is not None:
    for line in file_3_r:
        print(line.strip())
    print("Файл TF13_2.txt закрито!")
    file_3_r.close()

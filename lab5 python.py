schools = {
    "School_1": ("школа", 785),
    "School_2": ("школа", 520),
    "Technical_College_1": ("технікум",603),
    "College_2": ("технікум", 310),
    "University_1": ("університет",25000),
    "University_2": ("університет", 45000)
}

def Print(data):
    print("Перелік навчальних закладів:")
    for name, (type_, count) in data.items():
        print(f"{name}: тип – {type_}, кількість учнів – {count}")
    print()

def count_school_students(data):
    total = 0
    for name, (type_, count) in data.items():
        if type_ == "школа":
            total += count
    return total

Print(schools)

total_school = count_school_students(schools)
print("Загальна кількість учнів у школах:", total_school)

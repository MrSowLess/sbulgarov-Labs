groupmates = [
    {
        "name": "Михаил",
        "surname": "Шифутинский",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Александр",
        "surname": "Лукашенко",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Савелий",
        "surname": "Крамаров",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Алена",
        "surname": "Подъяпольская",
        "exams": ["Физика", "ИС", "ЭЭиС"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Александра",
        "surname": "Воробьева",
        "exams": ["Радиотехника", "ИС", "Web"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Анатолий",
        "surname": "Васерман",
        "exams": ["Философия", "АиГ", "ЭЭиС"],
        "marks": [2, 3, 4]
    }
]

input_score = float(input(u"Введите значение среднего балла: "))

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20), u"Средний балл")
    for student in students:
        sum_score = sum(student["marks"])
        average_score = sum_score / len(student["marks"])
        if average_score >= input_score:
            print(student["name"].ljust(15), student["surname"].ljust(10),
                str(student["exams"]).ljust(30),
                str(student["marks"]).ljust(20),
                f"{average_score:.2f}")

print_students(groupmates)
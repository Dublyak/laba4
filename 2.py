import random

def schedule_exams(count, subjects):
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    times = ["9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00", "13:30", "14:00"]
    for i in range(count):
        day = random.choice(days_of_week)
        time = random.choice(times)
        lucky_ticket = random.randint(1, 20)
        print(f"Экзамен по дисциплине «{subjects[i]}» состоится в {day} в {time}. Ваш счастливый билет N {lucky_ticket}.")

exam_count = int(input("Введите количество экзаменов: "))
subjects_input = input("Введите названия дисциплин через запятую: ")
subjects = [subject.strip() for subject in subjects_input.split(',')]
schedule_exams(exam_count, subjects)

from datetime import datetime, timedelta

def exam_date(days_until_exam):
    today = datetime.now()
    exam_day = today + timedelta(days=days_until_exam)
    return exam_day.strftime("%d %B")

K = int(input("Введите количество дней до экзамена: "))
print(f"Экзамен состоится {exam_date(K)}.")

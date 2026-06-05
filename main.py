from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

if __name__ == '__main__':
    print(f"Текущая дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    calculate_salary()
    get_employees()
    print("Программа завершена.")

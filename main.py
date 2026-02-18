from application.salary import calculate_salaru
from application.db.people import get_employees
from datetime import datetime


if __name__ == '__main__':
    print(datetime.now().date())
    calculate_salaru()
    get_employees()
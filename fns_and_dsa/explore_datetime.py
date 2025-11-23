from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")


def calculate_future_date():
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    future_date = datetime.now() + timedelta(days = number_of_days)
    return future_date.strftime('%Y-%m-%d')

print(display_current_datetime())

print(calculate_future_date())
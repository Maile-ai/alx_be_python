from datetime import datetime
from datetime import timedelta

current_date = datetime.now()
format_str = "%Y-%m-%d %H:%M:%S"

def display_current_datetime():
    formatted_date = current_date.strftime(format_str)
    print("Current date and time:", formatted_date)

def calculate_future_date():
    days_to_add = int(input("Enter number of days to add: ")) 
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime(format_str)
    print(f"Future date:", formatted_future_date)


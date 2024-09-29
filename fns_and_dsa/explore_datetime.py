from datetime import datetime, timedelta

# Part 1: Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate Future Date
def calculate_future_date(current_date):
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

# Main Execution
if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)

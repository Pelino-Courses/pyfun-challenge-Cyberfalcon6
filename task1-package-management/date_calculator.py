from datetime import date, datetime

def date_diff(date1:str, date2:str):
    if not isinstance(date1, str):
        raise TypeError("all arguments should be string")
    date1_formatted = datetime.strptime(date1, "%Y-%m-%d")
    if not isinstance(date2, str):
        raise TypeError("all arguments should be string")
    date2_formatted = datetime.strptime(date2, "%Y-%m-%d")
    return abs((date2_formatted - date1_formatted).days)

if __name__ == "__main__":
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")
    try:
        difference = date_diff(date1, date2)
        print(f"The difference between the two dates is {difference} days.")
    except Exception as e:
        print(f"Error: {e}")
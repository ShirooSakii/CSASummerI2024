# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

minutes_input = input("Enter the number of minutes: ")

minutes = int(minutes_input)
Total_days = minutes // (60*24)
years = Total_days // 365
Remaining_days = Total_days % 365 

print(f"{minutes}  minutes is approximately {years} years and {Remaining_days} days.")
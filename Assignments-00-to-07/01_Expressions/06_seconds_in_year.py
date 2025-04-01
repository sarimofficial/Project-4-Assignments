# Constants
REGULAR_YEAR_DAYS = 365
LEAP_YEAR_DAYS = 366
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

# Calculation with choice
year_type = input("Is it a leap year? (yes/no): ").lower()
days = LEAP_YEAR_DAYS if year_type == "yes" else REGULAR_YEAR_DAYS
seconds = days * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

print(f"There are {seconds:,} seconds in this year!")
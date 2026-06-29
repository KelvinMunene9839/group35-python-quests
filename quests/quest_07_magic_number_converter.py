# Quest 7: The Magic Number Converter
# Concept: Type Conversion - input() always gives a string, so convert to int for math.

birth_year = int(input("What year were you born? "))
current_year = 2025

age = current_year - birth_year

print(f"You were born in {birth_year}, so you are approximately {age} years old.")

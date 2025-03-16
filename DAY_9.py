# 🚀 Mission:
# Create a simple program that calculates a person’s age based on their birth year.

from datetime import datetime

# 🚀 Mission Start
print("\n\t\t\t🕒 Welcome to the Age Calculator! 🎂\n")

# 💡 Get user input
birth_date = input("📅 Enter your birthdate (DD/MM/YYYY): ")

# ✅ Check for valid input
try:
    birth_date = datetime.strptime(birth_date, "%d/%m/%Y")  # Convert string to date
    current_date = datetime(2025, 3, 13)  # Assume today's date in 2025

    # 🛑 Check if birthdate is in the future
    if birth_date > current_date:
        print("\n⚠️ Error: You entered a future birthdate! Please enter a valid past date. ❌")
    else:
        # Calculate age
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        print(f"\n🎉 You are {age} years old! 🎂")

        # 🎯 Bonus: How many years left until 100?
        years_left = 100 - age
        if years_left > 0:
            print(f"\n🕰️  You have {years_left} years left until you turn 100! 💯")
        else:
            print("\n💯 Wow! You have already reached 100 years or more! 🥳")

except ValueError:
    print("\n⚠️ Invalid input! Please enter your birthdate in DD/MM/YYYY format. ❌")

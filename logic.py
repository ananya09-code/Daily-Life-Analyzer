import os
import csv
from datetime import datetime

FILE_NAME = "daily_life.csv"
MOODS = ["bad", "okay", "good"]


def add_daily():
    file_exists = os.path.isfile(FILE_NAME)

    today = datetime.today().strftime("%Y-%m-%d")
    date = input("Enter date (YYYY-MM-DD) [default today]: ") or today
    sleep_hours = float(input("Sleep hours: "))

    while True:
        mood = input("Mood (bad, okay, good): ").lower()
        if mood in MOODS:
            break
        print("Invalid mood. Choose: bad, okay, good")

    money_spent = float(input("Money spent: ") or 0)
    notes = input("Notes (optional): ") or ""

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["date", "mood", "sleep_hours", "money_spent", "notes"])
        writer.writerow([date, mood, sleep_hours, money_spent, notes])

    print("Entry saved successfully!")


def show_daily():
    if not os.path.isfile(FILE_NAME):
        print("No entries found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader, None)

        if not header:
            print("No entries found.")
            return

        print(f"{'Date':<12}{'Mood':<8}{'Sleep':<8}{'Money':<10}{'Notes':<20}")
        print("-" * 58)

        has_data = False
        for row in reader:
            has_data = True
            print(f"{row[0]:<12}{row[1]:<8}{row[2]:<8}{row[3]:<10}{row[4]:<20}")

        if not has_data:
            print("No entries found.")


def summary_daily():
    if not os.path.isfile(FILE_NAME):
        print("No entries to analyze.")
        return

    total_money = 0
    total_sleep = 0
    entry_count = 0

    mood_count = {mood: 0 for mood in MOODS}
    money_by_mood = {mood: 0 for mood in MOODS}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            entry_count += 1
            mood = row[1]
            sleep = float(row[2])
            money = float(row[3])

            total_sleep += sleep
            total_money += money
            mood_count[mood] += 1
            money_by_mood[mood] += money

    if entry_count == 0:
        print("No entries to analyze.")
        return

    print("\n📊 Analysis")
    print(f"Average sleep: {total_sleep / entry_count:.2f} hours")
    print(f"Total money spent: {total_money}")

    print("\nMood breakdown:")
    for mood in MOODS:
        print(f"{mood}: {mood_count[mood]} days")

    print("\nMoney spent by mood:")
    for mood in MOODS:
        print(f"{mood}: {money_by_mood[mood]}")


def main():
    while True:
        print("\nDaily Life Analyzer")
        print("--------------------")
        print("1. Add daily entry")
        print("2. View all entries")
        print("3. Show analysis")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_daily()
        elif choice == "2":
            show_daily()
        elif choice == "3":
            summary_daily()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

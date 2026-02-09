import os
import csv
from datetime import datetime
file_name="daily_life.csv"
def add_daily():
     file_exists = os.path.isfile(file_name)
     today= datetime.today().strftime('%Y-%m-%d')
     date = input("Enter Date (YYYY-MM-DD): ") or today
     sleep_hours = float(input("Amount: "))
     while True:
         mood = input("mood (bad,good,okey): ").lower()
         if mood in ["bad","good","okey"]:
             break
         else:
             print("invaled input try[bad,good,okey]")

     money_spent=float(input("how much did you spend: ")) or 0
     notes= input("Description: ") or "emptiy"

     with open(file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["date","mood","sleep_hours","money_spent","notes"])

        writer.writerow([date, mood, sleep_hours, money_spent,notes])

     print("Expense added successfully!")

    

   











while True:
    print("welcome to daily_life.csv")
    print("------------------------------")
    print("1.Add daily entry")
    print("2.View all entries")
    print("3.Show analysis")
    print("4.exit")
    print("------------------------------")
    choice=int(input("enter your choose: "))
    if choice==4:
        print("goodbye......")
        break
    elif choice==1:
        add_daily()

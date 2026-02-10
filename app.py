from flask import Flask, render_template, request, redirect, url_for
import csv
import os
from datetime import datetime

app = Flask(__name__)
FILE_NAME = "daily_life.csv"


def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "mood", "sleep", "money", "notes"])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_daily():
    if request.method == "POST":
        date = request.form.get("date") or datetime.today().strftime("%Y-%m-%d")
        mood = request.form.get("mood")
        sleep = float(request.form.get("sleep_hours"))
        money = float(request.form.get("money_spent"))
        notes = request.form.get("notes")

        with open(FILE_NAME, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date, mood,sleep, money, notes])

        return redirect(url_for("view_daily"))

    return render_template("add.html")


@app.route("/view")
def view_daily():
    entries = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            reader = csv.DictReader(f)
            entries = list(reader)

    return render_template("view.html", entries=entries)


@app.route("/summary")
def summary_daily():
    total_money = 0.0
    total_sleep = 0.0
    mood_count = {"bad": 0, "good": 0, "okey": 0}

    with open(FILE_NAME, newline="") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
         money = row.get("money_spent", "").strip()
         sleep = row.get("sleep_hours", "").strip()
         mood = row.get("mood", "").lower()

         total_money += float(money) if money else 0.0
         total_sleep += float(sleep) if sleep else 0.0

         if mood in mood_count:
             mood_count[mood] += 1

             
    return render_template(
        "summary.htm",
        total_money=total_money,
        total_sleep=total_sleep,
        mood_count=mood_count
    )

  
  

    


if __name__ == "__main__":
    init_file()
    app.run(debug=True)

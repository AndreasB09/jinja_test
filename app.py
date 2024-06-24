from flask import Flask, render_template
import calendar
from datetime import datetime

app = Flask(__name__)

def create_calendar(year, month):
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    return month_days

@app.route('/')
def home():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    calendar_data = create_calendar(year, month)
    week_days = [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render_template(
        'calendar.html',
        title="Calendar",
        header=f"{day} {calendar.month_name[month]} {year}",
        week_days=week_days,
        calendar=calendar_data,
        current_day=day
    )

if __name__ == "__main__":
    app.run(debug=True)
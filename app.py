from flask import Flask, render_template, request
import calendar
from datetime import datetime

app = Flask(__name__)

def create_calendar(year, month):
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    return month_days

@app.route('/', methods=['GET'])
def home():
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day

    selected_year = request.args.get('year', current_year, type=int)
    selected_month = request.args.get('month', current_month, type=int)

    calendar_data = create_calendar(selected_year, selected_month)
    week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    header = f"{current_day} {calendar.month_name[current_month]} {current_year}"

    return render_template(
        'calendar.html',
        title="Calendar",
        header=header,
        week_days=week_days,
        calendar=calendar_data,
        current_day=current_day,
        current_month=current_month,
        current_year=current_year,
        selected_month=selected_month,
        selected_year=selected_year,
        calendar_module=calendar
    )

if __name__ == "__main__":
    app.run(debug=True)
import datetime


def get_fridays_and_saturdays(start_date, end_date):
    dates = []
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() == 4:  # 4 represents Friday (Monday is 0)
            dates.append(current_date)
        elif current_date.weekday() == 5:  # 5 represents Saturday
            dates.append(current_date)

        current_date += datetime.timedelta(days=1)

    return dates


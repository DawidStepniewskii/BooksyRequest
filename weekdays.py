import datetime


def get_fridays_and_saturdays(start_date: datetime, end_date: datetime) -> datetime:
    dates = []

    while start_date <= end_date:
        if start_date.weekday() in [4, 5]:  # 4 represents Friday, 5 represents Saturday
            for hour in range(8, 16):
                for minute in range(0, 60, 15):  # Every 15 minutes
                    current_datetime = datetime.datetime(
                        start_date.year,
                        start_date.month,
                        start_date.day,
                        hour,
                        minute
                    )
                    dates.append(str(current_datetime))
        start_date += datetime.timedelta(days=1)

    return dates

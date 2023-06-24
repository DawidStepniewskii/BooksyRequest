import asyncio
import datetime
import time

from dateutil.relativedelta import relativedelta
import weekdays
import http_request, prepare_data


def main():
    url = "https://pl.booksy.com/api/pl/2/customer_api/me/appointments/business/103502/dry_run/"

    headers = {
        "Content-Type": "application/json",
        "x-api-key": "web-e3d812bf-d7a2-445d-ab38-55589ae6a121"
    }

    start_date = datetime.date.today()
    end_date = start_date + relativedelta(months=1)
    dates = weekdays.get_fridays_and_saturdays(start_date, end_date)

    throttler = http_request.RequestThrottler(rate_limit=10, interval=60)

    data_with_body = prepare_data.create_data_with_body(dates)

    responses = []
    for data in data_with_body:
        response = throttler.make_request(url=url, headers=headers, data=data)
        responses.append(response)
        print(response)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed Time: {:.2f} seconds".format(elapsed_time))

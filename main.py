import datetime
import json
import requests
import get_weekdays
from dateutil.relativedelta import relativedelta

start_date = datetime.date.today()
end_date = start_date + relativedelta(months=1)
weekdays = get_weekdays.get_fridays_and_saturdays(start_date, end_date)


url = "https://pl.booksy.com/api/pl/2/customer_api/me/appointments/business/103502/dry_run/"

headers = {
    "Content-Type": "application/json",
    "x-api-key": "web-e3d812bf-d7a2-445d-ab38-55589ae6a121"
}

data = {
    "subbookings": [
        {
            "staffer_id": 199422,
            "booked_from": "2023-06-30 11:00",
            "service_variant": {
                "mode": "variant",
                "id": 4028268
            },
            "combo_children": []
        }
    ],
    "compatibilities": {
        "prepayment": True
    }
}

# response = requests.post(url, headers=headers, data=json.dumps(data))
#
# http_code = response.status_code
#
# print("HTTP Status Code:", http_code)


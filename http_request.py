from datetime import datetime
from typing import List
from tqdm import tqdm

import requests
import json


def generate_request(booked_from: str) -> List[str]:
    available_date = []
    progress_bar = tqdm(total=len(booked_from))

    url = "https://pl.booksy.com/api/pl/2/customer_api/me/appointments/business/103502/dry_run/"

    headers = {
        "Content-Type": "application/json",
        "x-api-key": "web-e3d812bf-d7a2-445d-ab38-55589ae6a121"
    }

    for i, date in enumerate(booked_from):
        data = {
            "subbookings": [
                {
                    "staffer_id": 199422,
                    "booked_from": date,
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

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 201:
            available_date.append(date)

        progress_bar.update(1)

    return available_date

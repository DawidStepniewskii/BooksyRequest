def create_data_with_body(booked_from: str):
    data_with_body = []

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
        data_with_body.append(data)

    return data_with_body

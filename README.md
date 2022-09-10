# fly-high

* Clone repository
* run `pip install`
* run `python app.py`

server will start on `http://127.0.0.1:5000`

Python version used `3.8.12`

API endpoint:

* `http://127.0.0.1:5000/plan` : POST request to search the trip details.
  * Request:
    ```
      {
        "source": "OBY"
      }
    ```

  * Response:
    ```
    {
        "data": {
            "total_distance": 41129.72,
            "trip_details": [
                {
                    "order": 0,
                    "id": "OBY",
                    "name": "Ittoqqortoormiit",
                    "location": {
                        "lat": 70.4856,
                        "lon": -21.9629
                    },
                    "country_name": "",
                    "country_id": "",
                    "images": [],
                    "contId": "north-america"
                },
                {
                    "order": 1,
                    "id": "IFJ",
                    "name": "Ísafjörður",
                    "location": {
                        "lat": 66.061106,
                        "lon": -23.18886
                    },
                    "country_name": "",
                    "country_id": "",
                    "images": [],
                    "contId": "europe",
                    "distance_from_previous_location": "494.54",
                    "distance_unit": "kms"
                },
                {
                    "order": 2,
                    "id": "SBT",
                    "name": "Sabetta",
                    "location": {
                        "lat": 71.251111,
                        "lon": 72.101667
                    },
                    "country_name": "",
                    "country_id": "",
                    "images": [],
                    "contId": "asia",
                    "distance_from_previous_location": "3492.70",
                    "distance_unit": "kms"
                },
                {
                    "order": 3,
                    "id": "ALY",
                    "name": "Alexandria",
                    "location": {
                        "lat": 31.200092,
                        "lon": 29.918739
                    },
                    "country_name": "",
                    "country_id": "",
                    "images": [],
                    "contId": "africa",
                    "distance_from_previous_location": "5118.44",
                    "distance_unit": "kms"
                },
                {
                    "order": 4,
                    "id": "FEN",
                    "name": "Fernando de Noronha",
                    "location": {
                        "lat": -3.85763,
                        "lon": -32.429737
                    },
                    "country_name": "",
                    "country_id": "",
                    "images": [],
                    "contId": "south-america",
                    "distance_from_previous_location": "7653.00",
                    "distance_unit": "kms"
                },
                {
                    "order": 5,
                    "id": "GMR",
                    "name": "Totegegie",
                    "location": {
                        "lat": -23.08,
                        "lon": -134.89028
                    },
                    "country_name": "",
                    "country_id": "",
                    "images": [
                        "12.JPG",
                        "13.jpg"
                    ],
                    "contId": "oceania",
                    "distance_from_previous_location": "11106.72",
                    "distance_unit": "kms"
                },
                {
                    "order": 6,
                    "id": "OBY",
                    "name": "Ittoqqortoormiit",
                    "location": {
                        "lat": 70.4856,
                        "lon": -21.9629
                    },
                    "country_name": "",
                    "country_id": "",
                    "images": [],
                    "contId": "north-america",
                    "distance_from_previous_location": "13264.32",
                    "distance_unit": "kms"
                }
            ]
        },
        "status": "SUCCESS",
        "message": "Trip planned successfully"
    }
    ```

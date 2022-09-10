import json
from turtle import distance
import mpu

from src.dto.request.plan import PlanRequestDTO

from base_constants import app_root

class PlanService:

    def __init__(self) -> None:
        
        self.cities = self.__get_cities()

    def get_trip_plan_for_source(self, plan_request: PlanRequestDTO):
        
        source_details = self.__fetch_city_details(city_id=plan_request.source)
        
        trip_details = self.__get_trip_details(source_details)

        total_distance = self.__get_total_distance_covered(trip_details)

        return {
            "total_distance": "{:.2f}".format(total_distance),
            "trip_details": trip_details
        }

    def __get_trip_details(self, source_details):

        planned_cities = []
        source_order = 0
        continents_covered = [source_details.get("contId")]

        planned_cities.append({
            "order": source_order,
            "id": source_details.get("id", ""),
            "name": source_details.get("name", ""),
            "location": source_details.get("location", ""),
            "country_name": source_details.get("country_name", ""),
            "country_id": source_details.get("country_id", ""),
            "images": source_details.get("images", ""),
            "contId": source_details.get("contId", "")
        })

        planned_cities = self.__fetch_nearest_city(source_details, continents_covered, planned_cities, source_order+1)

        planned_cities = self.__add_final_destination(source_details, planned_cities)

        return planned_cities
        
    def __fetch_city_details(self, city_id):

        if city_id not in self.cities.keys():
            raise Exception(f"Source not found in our Database for ID : {city_id}");
        
        return self.cities.get(city_id)

    def __get_cities(self):
        
        cities = open(f'{app_root}/src/static/cities.json')

        return json.load(cities)

    def __get_distance_using_longitude_latitude(self, long1, long2, lat1, lat2):
        return mpu.haversine_distance((lat1, long1), (lat2, long2))

    def __fetch_nearest_city(self, source_details, continents_covered, planned_cities, order):

        source_longitude = source_details.get("location").get("lon")
        source_latitude = source_details.get("location").get("lat")

        shortest_distance = None
        shortest_distant_city_id = None

        for city_id, city_details in self.cities.items():
            if city_id != source_details.get("id") and city_details.get("contId") not in continents_covered:
                distance_from_source = self.__get_distance_using_longitude_latitude(
                    source_longitude, 
                    city_details.get("location").get("lon"), 
                    source_latitude, 
                    city_details.get("location").get("lat")
                )

                if not shortest_distance or distance_from_source < shortest_distance:
                    shortest_distance = distance_from_source
                    shortest_distant_city_id = city_id

        nearest_city = self.__fetch_city_details(shortest_distant_city_id)
        continents_covered.append(nearest_city.get("contId"))
        planned_cities.append({
            "order": order,
            "id": nearest_city.get("id", ""),
            "name": nearest_city.get("name", ""),
            "location": nearest_city.get("location", ""),
            "country_name": nearest_city.get("country_name", ""),
            "country_id": nearest_city.get("country_id", ""),
            "images": nearest_city.get("images", ""),
            "contId": nearest_city.get("contId", ""),
            "distance_from_previous_location": "{:.2f}".format(shortest_distance),
            "distance_unit": "kms"
        })
        
        if (len(continents_covered) < 6):
            planned_cities = self.__fetch_nearest_city(nearest_city, continents_covered, planned_cities, order+1)
        
        return planned_cities

    def __add_final_destination(self, source, trip_order):

        distance = self.__get_distance_using_longitude_latitude(
            source.get("location").get("lon"), 
            trip_order[len(trip_order) - 1].get("location").get("lon"), 
            source.get("location").get("lat"), 
            trip_order[len(trip_order) - 1].get("location").get("lat")
        )

        trip_order.append({
            "order": len(trip_order),
            "id": source.get("id", ""),
            "name": source.get("name", ""),
            "location": source.get("location", ""),
            "country_name": source.get("country_name", ""),
            "country_id": source.get("country_id", ""),
            "images": source.get("images", ""),
            "contId": source.get("contId", ""),
            "distance_from_previous_location": "{:.2f}".format(distance),
            "distance_unit": "kms"
        })

        return trip_order

    def __get_total_distance_covered(self, trip_details):
        return sum(float(trip.get("distance_from_previous_location", 0)) for trip in trip_details)
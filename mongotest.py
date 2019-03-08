import pymongo
from pymongo import MongoClient
from math import sqrt
from geopy.distance import geodesic

client = MongoClient("mongodb://localhost:27017")

db = client.bikerackputter

restaurants = db.restaurants.find({})

restaurants_by_need = db.restaurants_by_need_full

restaurants_located = []
for restaurant in restaurants:
    distances = []
    bikeracks = db.bikeracks.find({})
    for bikerack in bikeracks:
        distances.append(
            {
                "distance": geodesic(
                    (bikerack["y"], bikerack["x"]),
                    (
                        restaurant["coordinates"]["latitude"],
                        restaurant["coordinates"]["longitude"],
                    ),
                ).feet,
                "bikerack": bikerack,
            }
        )
    distances_sorted = sorted(distances, key=lambda k: k["distance"])

    restaurants_by_need.insert_one(
        {
            "name": restaurant["name"],
            "ratings": restaurant["review_count"],
            "details": restaurant,
            "distances": distances_sorted[:5],
            "need": restaurant["review_count"] * distances_sorted[0]["distance"],
        }
    )


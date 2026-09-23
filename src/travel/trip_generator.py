from itertools import product

def generate_trip_options():
    destinations = ["Brussels", "Luxembourg", "Amsterdam"]
    return [
        {"destination": d, "nights": n, "transport_cost": 0,
         "accommodation_cost": 0, "local_transport": 0, "total_cost": 0}
        for d, n in product(destinations, [2, 3, 4, 5])
    ]

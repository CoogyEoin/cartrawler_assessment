from modules import cars

API_OBJECT = {
        "GET":{
                "test": cars.test,
                "remove_duplicates": cars.remove_duplicates,
                "call_endpoint": cars.call_endpoint,
                "get_cheapest_of_each_car": cars.get_cheapest_of_each_car,
                "filter_cdar_cars": cars.filter_cdar_cars,
                "get_corporate_cars": cars.get_corporate_cars,
                "sort_low_to_high_by_group": cars.sort_low_to_high_by_group
        },
        "POST": {},
        "PUT": {},
        "DELETE": {}
}

import json
from handlers.request_handler import RequestHandler

def test():
    return "This is a test"


def call_endpoint():
    '''
    Returns the first element of the array returned by the endpoint. 
    '''
    obj = RequestHandler()
    return json.loads(obj.make_get_request())


def remove_duplicates():
    car_list = []
    car_types = []
    resp = call_endpoint()
    for vendor in resp[0]['VehAvailRSCore']['VehVendorAvails']:
        for car in vendor['VehAvails']:
            if car['Vehicle']['VehMakeModel'] in car_types:
                continue
            car_list.append(car)
            car_types.append(car['Vehicle']['VehMakeModel'])
    return car_list


def get_cheapest_of_each_car():
    car_list = []
    car_types = []
    price_obj = {}
    resp = call_endpoint()
    for vendor in resp[0]['VehAvailRSCore']['VehVendorAvails']:
        for car in vendor['VehAvails']:
            model = car['Vehicle']['VehMakeModel']['@Name']
            cost = car['TotalCharge']['@EstimatedTotalAmount']
            if model in car_types: 
                if float(cost) < float(price_obj[model]):
                    car_list.append(car)
                    price_obj[model] = cost
                continue
            car_list.append(car)
            price_obj[model] = car['TotalCharge']['@EstimatedTotalAmount']
            car_types.append(car['Vehicle']['VehMakeModel'])
    return car_list

def filter_cdar_cars():
    car_list = []
    resp = call_endpoint()
    for vendor in resp[0]['VehAvailRSCore']['VehVendorAvails']:
        for car in vendor['VehAvails']:
            if car['Vehicle']['@Code'] != "CDAR":
                car_list.append(car)
    return car_list


def get_corporate_cars():
    car_list = []
    resp = call_endpoint()
    for vendor in resp[0]['VehAvailRSCore']['VehVendorAvails']:
        if vendor['Vendor']['@Name'] in ['AVIS', 'ALAMO']:
            for car in vendor['VehAvails']:
                if car['Vehicle']['VehMakeModel']:
                    car_list.append(car)
    return car_list


def sort_low_to_high_by_group():
    car_dict = {}
    resp = call_endpoint()
    for vendor in resp[0]['VehAvailRSCore']['VehVendorAvails']:
        group = vendor['Vendor']['@Name']
        vendor_car_list = []
        for car in vendor['VehAvails']:
            #cost = car['TotalCharge']['@EstimatedTotalAmount']
            vendor_car_list.append(car)
        car_dict[group] = sorted(vendor_car_list, key=lambda k: float(k['TotalCharge']['@EstimatedTotalAmount']))
    return car_dict

# CarTrawler Code Assessment

This is my repo containing the code for the API assessment. I attempted to do this assignment in javascript ([can be seen in this repo](https://github.com/CoogyEoin/cartrawler_javascript_attempt))but the asynchrounous nature of the language caused too many difficulties for me so I decided to switch to using python on the third day and managed to get a working application. This lead to some shortcomings which I will discuss in the "nice to haves" section.


## Overview

This is an API application that runs on localhost port 8080. It has a single endpoint called /cars that takes a "method" keyword parameter in the request body. This endpoint calls the example CarTrawler API (https://www.cartrawler.com/ctabe/cars.json) and performs various actions on the data depending on the method specified. The valid methods are listed below.

* test: Simply returns a string saying "This is a test".
* remove_duplicates: Returns a list of cars with duplicate car models removed.
* call_endpoint: Calls the example cartrawler API and returns an unaltered JSON response.
* get_cheapest_of_each_car: Returns a list of cars with the cheapest of each model present in case of duplicates.
* filter_cdar_cars: Returns a list of cars with the vehicles containing the CDAR code filtered out.
* get_corporate_cars: Returns a list of all cars in the AVIS and ALAMO vendor groups.
* sort_low_to_high_by_group: Returns a JSON object of each group with their cars sorted from price low to high.
 
